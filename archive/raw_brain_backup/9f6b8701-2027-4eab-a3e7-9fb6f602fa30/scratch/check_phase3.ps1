$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\3 In Goal Air Force"
$gDriveFolder = "G:\My Drive\Pp another folder"

$localFiles = Get-ChildItem -Path $localFolder -File
$gDriveFiles = Get-ChildItem -Path $gDriveFolder -File

$localBaseNames = @{}
foreach ($file in $localFiles) {
    $localBaseNames[$file.BaseName] = $true
}

$matchedCount = 0
$unmatchedCount = 0

foreach ($file in $gDriveFiles) {
    if ($localBaseNames.ContainsKey($file.BaseName)) {
        $matchedCount++
    } else {
        $unmatchedCount++
    }
}

Write-Host "Matched files (to delete): $matchedCount"
Write-Host "Unmatched files (to keep): $unmatchedCount"
