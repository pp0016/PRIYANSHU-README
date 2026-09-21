$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\1 In Education with Toddlers"
$files = @(
    "lv_0_20250906220255.mp4",
    "lv_0_20250928013014.mp4",
    "VID20240701182320.mp4",
    "VID20241027144628.mp4",
    "VID20241027144756.mp4",
    "VID20241108070225.mp4",
    "VID20241127095543.mp4",
    "VID20250815211625.mp4",
    "VID20250815211725.mp4",
    "VID_20260128093713.mp4"
)

$totalSize = 0
foreach ($file in $files) {
    $filePath = Join-Path -Path $localFolder -ChildPath $file
    if (Test-Path -LiteralPath $filePath) {
        $size = (Get-Item -LiteralPath $filePath).Length
        $totalSize += $size
    }
}

$sizeMB = [math]::Round($totalSize / 1MB, 2)
Write-Host "Total size: $sizeMB MB"
