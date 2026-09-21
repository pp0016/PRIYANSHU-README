$sourceDir = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive"
$destDir = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed"

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

$extensions = @(".mp4", ".mkv", ".avi", ".mov", ".wmv", ".flv", ".webm", ".m4v", ".3gp")
$files = Get-ChildItem -Path $sourceDir -File -Recurse | Where-Object { $extensions -contains $_.Extension.ToLower() }
$total = $files.Count
$count = 0

Write-Host "Found $total video files to compress."

foreach ($file in $files) {
    $count++
    $relativePath = $file.FullName.Substring($sourceDir.Length + 1)
    $destPath = Join-Path -Path $destDir -ChildPath $relativePath
    $destFolder = Split-Path -Path $destPath -Parent
    
    if (-not (Test-Path $destFolder)) {
        New-Item -ItemType Directory -Path $destFolder | Out-Null
    }
    
    # Change extension to .mp4
    $destPath = [System.IO.Path]::ChangeExtension($destPath, ".mp4")
    
    if (Test-Path $destPath) {
        $existingSize = (Get-Item $destPath).Length
        if ($existingSize -gt 0) {
            Write-Host "[$count/$total] Skipping already existing: $relativePath"
            continue
        }
    }
    
    Write-Host "[$count/$total] Compressing: $relativePath ($([math]::Round($file.Length / 1MB, 2)) MB)"
    
    # Run FFmpeg with error level logging to prevent massive log files
    $ffmpegArgs = @(
        "-v", "error",
        "-y",
        "-nostdin",
        "-i", $file.FullName,
        "-c:v", "libx264",
        "-crf", "28",
        "-preset", "fast",
        "-c:a", "aac",
        "-b:a", "128k",
        $destPath
    )
    
    & ffmpeg @ffmpegArgs
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "Error compressing $relativePath"
    } else {
        $newSize = (Get-Item $destPath).Length
        $saved = $file.Length - $newSize
        $savedPercent = [math]::Round(($saved / $file.Length) * 100, 2)
        Write-Host "  -> Done! New size: $([math]::Round($newSize / 1MB, 2)) MB (Saved $savedPercent%)"
    }
}
Write-Host "Compression completed."
