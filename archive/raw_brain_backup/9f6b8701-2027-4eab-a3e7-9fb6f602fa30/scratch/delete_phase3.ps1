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
$unmatchedSize = 0

Write-Host "--- Unmatched Files (Kept in Google Drive) ---"

foreach ($file in $gDriveFiles) {
    if ($localBaseNames.ContainsKey($file.BaseName)) {
        Remove-Item -LiteralPath $file.FullName -Force
        $matchedCount++
    } else {
        $sizeMB = [math]::Round($file.Length / 1MB, 2)
        Write-Host "- $($file.Name) (${sizeMB} MB)"
        $unmatchedSize += $file.Length
        $unmatchedCount++
    }
}

$totalUnmatchedMB = [math]::Round($unmatchedSize / 1MB, 2)
Write-Host "-----------------"
Write-Host "Done. Deleted: $matchedCount files."
Write-Host "Total space used by the 5 unmatched files: $totalUnmatchedMB MB."
