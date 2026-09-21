$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\1 In Education with Toddlers"
$gDriveFolder = "G:\My Drive\My top five most storage size videos\PP phones top 100 videos to give in Google Drive"

$localFiles = Get-ChildItem -Path $localFolder -File
$gDriveFiles = Get-ChildItem -Path $gDriveFolder -File

$localBaseNames = @{}
foreach ($file in $localFiles) {
    $localBaseNames[$file.BaseName] = $file
}

$gDriveBaseNames = @{}
foreach ($file in $gDriveFiles) {
    $gDriveBaseNames[$file.BaseName] = $file
}

$matchedCount = 0
$matchedSize = 0
$unmatchedGDriveCount = 0
$unmatchedGDriveSize = 0

Write-Host "--- Files in Google Drive NOT present in Local (Unmatched / Bigger files) ---"
foreach ($file in $gDriveFiles) {
    if ($localBaseNames.ContainsKey($file.BaseName)) {
        $matchedCount++
        $matchedSize += $file.Length
    } else {
        $sizeMB = [math]::Round($file.Length / 1MB, 2)
        Write-Host "- $($file.Name) (${sizeMB} MB)"
        $unmatchedGDriveCount++
        $unmatchedGDriveSize += $file.Length
    }
}

$unmatchedLocalCount = 0
Write-Host "`n--- Files in Local NOT present in Google Drive ---"
foreach ($file in $localFiles) {
    if (-not $gDriveBaseNames.ContainsKey($file.BaseName)) {
        Write-Host "- $($file.Name)"
        $unmatchedLocalCount++
    }
}

$matchedGB = [math]::Round($matchedSize / 1GB, 2)
$unmatchedGDriveGB = [math]::Round($unmatchedGDriveSize / 1GB, 2)

Write-Host "`n================================================"
Write-Host "DEEP CHECK SUMMARY:"
Write-Host "================================================"
Write-Host "Total Local Files: $($localFiles.Count)"
Write-Host "Total Google Drive Files: $($gDriveFiles.Count)"
Write-Host "------------------------------------------------"
Write-Host "MATCHED FILES (to be deleted from Google Drive):"
Write-Host "Count: $matchedCount files"
Write-Host "Space to be cleaned in Google Drive: $matchedGB GB"
Write-Host "------------------------------------------------"
Write-Host "UNMATCHED G-DRIVE FILES (kept in Google Drive):"
Write-Host "Count: $unmatchedGDriveCount files"
Write-Host "Space used: $unmatchedGDriveGB GB"
Write-Host "------------------------------------------------"
Write-Host "UNMATCHED LOCAL FILES (not in Google Drive):"
Write-Host "Count: $unmatchedLocalCount files"
Write-Host "================================================"
