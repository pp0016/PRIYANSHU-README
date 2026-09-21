$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\1 In Education with Toddlers"
$parentGDriveFolder = "G:\My Drive\My top five most storage size videos"

$filesToCheck = @(
    "Record_2024-01-21-20-38-06.mp4",
    "Record_2025-01-22-20-49-21.mp4",
    "VID20241127095543.mp4"
)

$matchedCount = 0
$unmatchedCount = 0

foreach ($file in $filesToCheck) {
    $localPath = Join-Path -Path $localFolder -ChildPath $file
    $gDrivePath = Join-Path -Path $parentGDriveFolder -ChildPath $file
    
    if (Test-Path -LiteralPath $localPath) {
        Write-Host "Matched (exists locally): $file"
        Remove-Item -LiteralPath $gDrivePath -Force
        $matchedCount++
    } else {
        $sizeMB = [math]::Round((Get-Item -LiteralPath $gDrivePath).Length / 1MB, 2)
        Write-Host "Unmatched (NOT local, please download): $file - Size: $sizeMB MB"
        $unmatchedCount++
    }
}

Write-Host "Done. Deleted $matchedCount matched files. Kept $unmatchedCount unmatched files."
