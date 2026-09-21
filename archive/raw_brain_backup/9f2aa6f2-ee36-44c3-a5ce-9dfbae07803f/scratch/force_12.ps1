param([int]$StartOffset=0, [int]$Count=3)

$fileList = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\final_12.txt"
$files = Get-Content $fileList | Select-Object -Skip $StartOffset -First $Count
$tempDir = "C:\mom phone storage compressed final"

if (!(Test-Path $tempDir)) { New-Item -ItemType Directory -Path $tempDir | Out-Null }

foreach ($relativePath in $files) {
    $originalPath = Join-Path "C:\mom phone storage" $relativePath
    if (!(Test-Path $originalPath)) { continue }
    
    $tempFile = Join-Path $tempDir (Split-Path $originalPath -Leaf)
    $ext = (Get-Item $originalPath).Extension.ToLower()
    
    $success = $false
    if ($ext -match '\.(mp4|mov|avi|mkv)$') {
        # Using H.264 (libx264) with extreme CRF 35 to guarantee shrinkage while staying 100% playable on Windows without paid codecs
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$originalPath`" -vcodec libx264 -crf 35 -preset ultrafast -y `"$tempFile`"" -Wait -NoNewWindow -PassThru
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    elseif ($ext -match '\.(jpg|jpeg|png)$') {
        if ($ext -eq ".png") { $tempFile = $tempFile -replace '\.png$', '.jpg' }
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$originalPath`" -q:v 25 -y `"$tempFile`"" -Wait -NoNewWindow -PassThru
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    
    if ($success -and (Test-Path $tempFile)) {
        $oldSize = (Get-Item $originalPath).Length
        $newSize = (Get-Item $tempFile).Length
        
        if ($newSize -lt $oldSize -and $newSize -gt 0) {
            Remove-Item -Path $originalPath -Force
            if ($tempFile -match '\.jpg$' -and $ext -eq '.png') {
                $targetPath = $originalPath -replace '\.png$', '.jpg'
            } else {
                $targetPath = $originalPath
            }
            Move-Item -Path $tempFile -Destination $targetPath -Force
            Write-Host "Success: $relativePath"
        } else {
            Remove-Item -Path $tempFile -Force
            Write-Host "Failed to make smaller: $relativePath"
        }
    }
}
