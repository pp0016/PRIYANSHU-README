$sourceDir = "C:\Users\renu5\Downloads\New folder\Instagram"
$destDir = "C:\Users\renu5\Downloads\New folder\Instagram compressed"

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Force -Path $destDir | Out-Null
}

$sourceFiles = Get-ChildItem -Path $sourceDir -File
$destFiles = Get-ChildItem -Path $destDir -File

$destNames = $destFiles | Select-Object -ExpandProperty Name
$remainingFiles = $sourceFiles | Where-Object { $destNames -notcontains $_.Name }

Write-Host "Total original files: $($sourceFiles.Count)"
Write-Host "Already compressed: $($destFiles.Count)"
Write-Host "Remaining to compress: $($remainingFiles.Count)"

$successCount = 0
$failCount = 0

foreach ($file in $remainingFiles) {
    $outPath = Join-Path $destDir $file.Name
    $ext = $file.Extension.ToLower()
    
    $attempt = 0
    $maxAttempts = 3
    $success = $false
    
    while ($attempt -lt $maxAttempts -and -not $success) {
        $attempt++
        Write-Host "Compressing $($file.Name) (Attempt $attempt)..."
        
        if ($ext -match "\.(mp4|mov|avi|mkv)$") {
            # Video
            $ffmpegArgs = "-i `"$($file.FullName)`" -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k -y `"$outPath`""
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList $ffmpegArgs -NoNewWindow -Wait -PassThru
        } elseif ($ext -match "\.(jpg|jpeg|png|heic|webp)$") {
            # Image
            $ffmpegArgs = "-i `"$($file.FullName)`" -q:v 5 -y `"$outPath`""
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList $ffmpegArgs -NoNewWindow -Wait -PassThru
        } else {
            # Copy other files
            Copy-Item -Path $file.FullName -Destination $outPath -Force
            $success = $true
            break
        }
        
        if (Test-Path $outPath) {
            $outFile = Get-Item $outPath
            if ($outFile.Length -gt 0) {
                $success = $true
            } else {
                Remove-Item $outPath -Force
            }
        }
    }
    
    if ($success) {
        $successCount++
    } else {
        $failCount++
        Write-Host "Failed to compress $($file.Name) after $maxAttempts attempts."
    }
}

$finalSourceFiles = Get-ChildItem -Path $sourceDir -File
$finalDestFiles = Get-ChildItem -Path $destDir -File

$origSize = ($finalSourceFiles | Measure-Object -Property Length -Sum).Sum
$newSize = ($finalDestFiles | Measure-Object -Property Length -Sum).Sum
$saved = $origSize - $newSize

Write-Host "--- SUMMARY ---"
Write-Host "Original Size: $origSize"
Write-Host "New Size: $newSize"
Write-Host "Space Saved: $saved"
Write-Host "Success: $successCount"
Write-Host "Failed: $failCount"
Write-Host "Total Successfully in Dest: $($finalDestFiles.Count)"
