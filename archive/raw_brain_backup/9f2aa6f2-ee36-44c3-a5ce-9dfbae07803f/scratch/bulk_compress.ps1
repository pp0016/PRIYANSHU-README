param(
    [int]$StartOffset = 0,
    [int]$Count = 0
)

$sourceDir = "C:\mom phone storage"
$destDir = "C:\mom phone storage compressed"
$deleteList = "$destDir\delete_list.md"

if (!(Test-Path $destDir)) { New-Item -ItemType Directory -Path $destDir | Out-Null }
if (!(Test-Path $deleteList)) { Set-Content -Path $deleteList -Value "# Safe to Delete`n" }

$files = Get-ChildItem -Path $sourceDir -File -Recurse | Where-Object { $_.Length -ge 1MB } | Sort-Object Length -Descending
$totalCount = $files.Count
if ($totalCount -eq 0) { exit }

$top20PercentCount = [math]::Round($totalCount * 0.2)
if ($top20PercentCount -eq 0) { $top20PercentCount = 1 }

$top20Files = $files | Select-Object -First $top20PercentCount

if ($Count -eq 0) { $Count = $top20PercentCount }

# Subset the files based on arguments
$subset = $top20Files | Select-Object -Skip $StartOffset -First $Count

Write-Host "Compressing $($subset.Count) files (from offset $StartOffset)..."

$current = 0
foreach ($file in $subset) {
    $current++
    $relativePath = $file.FullName.Substring($sourceDir.Length + 1)
    $destFile = Join-Path $destDir $relativePath
    $destFolder = Split-Path $destFile -Parent
    
    if (!(Test-Path $destFolder)) { New-Item -ItemType Directory -Path $destFolder | Out-Null }
    
    if (Test-Path $destFile) { 
        Write-Host "[$current/$($subset.Count)] Skipping: $($file.Name)"
        continue 
    }

    $ext = $file.Extension.ToLower()
    $success = $false
    Write-Host "[$current/$($subset.Count)] Compressing: $($file.Name)"

    if ($ext -match '\.(mp4|mov|avi|mkv)$') {
        $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$($file.FullName)`" -vcodec libx264 -crf 28 -preset fast -y `"$destFile`"" -Wait -NoNewWindow -PassThru
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    elseif ($ext -match '\.(jpg|jpeg|png|heic)$') {
        if ($ext -eq ".png") {
            $destFile = $destFile -replace '\.png$', '.jpg'
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$($file.FullName)`" -q:v 8 -y `"$destFile`"" -Wait -NoNewWindow -PassThru
        } else {
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-i `"$($file.FullName)`" -q:v 8 -y `"$destFile`"" -Wait -NoNewWindow -PassThru
        }
        if ($process.ExitCode -eq 0) { $success = $true }
    }
    
    if ($success) {
        Add-Content -Path $deleteList -Value "- $($file.FullName)"
    }
}
Write-Host "Finished processing chunk."
