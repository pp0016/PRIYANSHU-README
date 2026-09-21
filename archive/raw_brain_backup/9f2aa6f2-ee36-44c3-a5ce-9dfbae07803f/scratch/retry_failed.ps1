param([int]$StartOffset=0, [int]$Count=4)
$failedList = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\failed_files.txt"
$tempDir = "C:\mom phone storage compressed temp"

if (!(Test-Path $tempDir)) { New-Item -ItemType Directory -Path $tempDir | Out-Null }

$files = Get-Content $failedList | Select-Object -Skip $StartOffset -First $Count
$successCount = 0

foreach ($file in $files) {
    if (Test-Path $file) {
        $tempFile = Join-Path $tempDir (Split-Path $file -Leaf)
        Write-Host "Retrying compression for: $($file)"
        
        # Aggressive compression
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$file`" -vcodec libx264 -crf 32 -preset faster -y `"$tempFile`"" -Wait -NoNewWindow -PassThru
        
        if ($process.ExitCode -eq 0 -and (Test-Path $tempFile)) {
            $oldSize = (Get-Item $file).Length
            $newSize = (Get-Item $tempFile).Length
            
            if ($newSize -lt $oldSize -and $newSize -gt 0) {
                Remove-Item -Path $file -Force
                Move-Item -Path $tempFile -Destination $file -Force
                $successCount++
                Write-Host "Successfully force-compressed."
            } else {
                Remove-Item -Path $tempFile -Force
            }
        }
    }
}
Write-Host "Finished retrying. Succeeded: $successCount"
