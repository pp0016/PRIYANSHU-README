param([int]$StartOffset=0, [int]$Count=2663)

$sourceDir = "C:\mom phone storage"
$tempDir = "C:\mom phone storage compressed temp"
$verifiedList = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\verified_list.txt"

if (!(Test-Path $tempDir)) { New-Item -ItemType Directory -Path $tempDir | Out-Null }

# Load already processed files to exclude them
$excludeList = @(Get-Content $verifiedList)

Write-Host "Scanning for remaining files..."
# We only want files that we haven't processed yet
$allFiles = Get-ChildItem -Path $sourceDir -File -Recurse | Where-Object { 
    $_.Length -ge 1MB -and $excludeList -notcontains $_.FullName -and $_.FullName -notmatch "mom phone storage compressed"
}

$total = $allFiles.Count
Write-Host "Found $total remaining uncompressed files."

$subset = $allFiles | Select-Object -Skip $StartOffset -First $Count
Write-Host "Agent taking chunk of $($subset.Count) files."

$current = 0
foreach ($file in $subset) {
    $current++
    $tempFile = Join-Path $tempDir $file.Name
    $ext = $file.Extension.ToLower()
    $success = $false

    Write-Host "[$current/$($subset.Count)] Compressing: $($file.Name)"

    if ($ext -match '\.(mp4|mov|avi|mkv)$') {
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$($file.FullName)`" -vcodec libx264 -crf 28 -preset fast -y `"$tempFile`"" -Wait -NoNewWindow -PassThru
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    elseif ($ext -match '\.(jpg|jpeg|png|heic)$') {
        if ($ext -eq ".png") {
            $tempFile = $tempFile -replace '\.png$', '.jpg'
        }
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$($file.FullName)`" -q:v 8 -y `"$tempFile`"" -Wait -NoNewWindow -PassThru
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    
    if ($success -and (Test-Path $tempFile)) {
        $oldSize = $file.Length
        $newSize = (Get-Item $tempFile).Length
        
        # Only replace if actually smaller
        if ($newSize -lt $oldSize -and $newSize -gt 0) {
            $targetPath = $file.FullName
            if ($tempFile -match '\.jpg$' -and $file.Extension -eq '.png') {
                $targetPath = $targetPath -replace '\.png$', '.jpg'
                Remove-Item -Path $file.FullName -Force
            } else {
                Remove-Item -Path $file.FullName -Force
            }
            Move-Item -Path $tempFile -Destination $targetPath -Force
        } else {
            Remove-Item -Path $tempFile -Force
        }
    }
}
Write-Host "Agent finished its chunk."
