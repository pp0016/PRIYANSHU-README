$sourceDir = "C:\Users\renu5\OneDrive\Pictures\Camera imports"
$targetDir = "C:\Users\renu5\OneDrive\Pictures\Camera imports compressed"
$videoExtensions = @('.mp4', '.mov', '.avi', '.mkv', '.wmv', '.webm', '.m4v')
$imageExtensions = @('.jpg', '.jpeg', '.png', '.bmp', '.heic', '.webp')

Write-Output "Starting overnight ALL MEDIA compression script..."

if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

$allFiles = Get-ChildItem -Path $sourceDir -File -Recurse -ErrorAction SilentlyContinue
$total = $allFiles.Count
Write-Output "Found $total files to process."

$count = 0
$success = 0
$failed = 0
$copied = 0

foreach ($file in $allFiles) {
    $count++
    
    $relativePath = $file.FullName.Substring($sourceDir.Length).TrimStart('\', '/')
    $targetFilePath = Join-Path -Path $targetDir -ChildPath $relativePath
    $targetFileDir = Split-Path -Path $targetFilePath -Parent

    if (-not (Test-Path $targetFileDir)) {
        New-Item -ItemType Directory -Path $targetFileDir -Force | Out-Null
    }

    $ext = $file.Extension.ToLower()
    
    if (Test-Path $targetFilePath) {
        $existingSize = (Get-Item $targetFilePath).Length
        if ($existingSize -gt 0) {
            Write-Output "[$count/$total] Skipping existing: $($file.Name)"
            $success++
            continue
        }
    }

    Write-Output "[$count/$total] Processing: $($file.Name)"

    if ($videoExtensions -contains $ext) {
        $args = @("-y", "-v", "error", "-i", "`"$($file.FullName)`"", "-c:v", "libx264", "-crf", "28", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", "`"$targetFilePath`"")
        $proc = Start-Process -FilePath "ffmpeg" -ArgumentList $args -Wait -NoNewWindow -PassThru
        if ($proc.ExitCode -eq 0 -and (Test-Path $targetFilePath)) {
            $success++
            Write-Output " -> Video Success!"
        } else {
            Copy-Item -Path $file.FullName -Destination $targetFilePath -Force
            $copied++
            Write-Output " -> Video Failed! Copied original instead."
        }
    } elseif ($imageExtensions -contains $ext) {
        $args = @("-y", "-v", "error", "-i", "`"$($file.FullName)`"", "-q:v", "8", "`"$targetFilePath`"")
        $proc = Start-Process -FilePath "ffmpeg" -ArgumentList $args -Wait -NoNewWindow -PassThru
        if ($proc.ExitCode -eq 0 -and (Test-Path $targetFilePath)) {
            $newSize = (Get-Item $targetFilePath).Length
            if ($newSize -gt 0) {
                $success++
                Write-Output " -> Image Success!"
            } else {
                Copy-Item -Path $file.FullName -Destination $targetFilePath -Force
                $copied++
                Write-Output " -> Image resulted in 0 bytes! Copied original instead."
            }
        } else {
            Copy-Item -Path $file.FullName -Destination $targetFilePath -Force
            $copied++
            Write-Output " -> Image Failed! Copied original instead."
        }
    } else {
        Copy-Item -Path $file.FullName -Destination $targetFilePath -Force
        $copied++
        Write-Output " -> Unrecognized type. Copied original."
    }
}

Write-Output "----------------------------------------"
Write-Output "Processing complete!"
Write-Output "Total Files: $total"
Write-Output "Compressed Successfully: $success"
Write-Output "Copied Original: $copied"
