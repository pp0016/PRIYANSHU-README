$sourceDir = "C:\Users\renu5\OneDrive\Pictures\Camera imports"
$targetDir = "C:\Users\renu5\OneDrive\Pictures\Camera imports compressed"
$videoExtensions = @('.mp4', '.mov', '.avi', '.mkv', '.wmv', '.webm', '.m4v')

Write-Output "Starting overnight compression script..."
Write-Output "Source: $sourceDir"
Write-Output "Target: $targetDir"

if (-not (Test-Path $targetDir)) {
    New-Item -ItemType Directory -Path $targetDir -Force | Out-Null
}

$videoFiles = Get-ChildItem -Path $sourceDir -File -Recurse -ErrorAction SilentlyContinue | Where-Object { $videoExtensions -contains $_.Extension.ToLower() }
$total = $videoFiles.Count
Write-Output "Found $total videos to compress."

$count = 0
$success = 0
$failed = 0

foreach ($file in $videoFiles) {
    $count++
    
    # Calculate relative path safely
    $relativePath = $file.FullName.Substring($sourceDir.Length).TrimStart('\', '/')
    $targetFilePath = Join-Path -Path $targetDir -ChildPath $relativePath
    $targetFileDir = Split-Path -Path $targetFilePath -Parent

    if (-not (Test-Path $targetFileDir)) {
        New-Item -ItemType Directory -Path $targetFileDir -Force | Out-Null
    }

    Write-Output "[$count/$total] Compressing: $($file.Name)"
    
    $args = @(
        "-y", 
        "-i", "`"$($file.FullName)`"", 
        "-c:v", "libx264", 
        "-crf", "28", 
        "-preset", "fast", 
        "-c:a", "aac", 
        "-b:a", "128k", 
        "`"$targetFilePath`""
    )
    
    $proc = Start-Process -FilePath "ffmpeg" -ArgumentList $args -Wait -NoNewWindow -PassThru
    
    if ($proc.ExitCode -eq 0 -and (Test-Path $targetFilePath)) {
        $success++
        Write-Output " -> Success!"
    } else {
        $failed++
        Write-Output " -> Failed! Exit code: $($proc.ExitCode)"
    }
}

Write-Output "----------------------------------------"
Write-Output "Compression complete!"
Write-Output "Total: $total"
Write-Output "Success: $success"
Write-Output "Failed: $failed"
