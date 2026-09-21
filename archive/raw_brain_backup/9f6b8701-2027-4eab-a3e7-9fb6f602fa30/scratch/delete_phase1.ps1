$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\2 Priyansu Prajapati 2017"
$gDriveFolder = "G:\My Drive\pp phones all the videos"

$localFiles = Get-ChildItem -Path $localFolder -File
$gDriveFiles = Get-ChildItem -Path $gDriveFolder -File

$localBaseNames = @{}
foreach ($file in $localFiles) {
    $localBaseNames[$file.BaseName] = $true
}

$deletedCount = 0
$skippedCount = 0

foreach ($file in $gDriveFiles) {
    if ($localBaseNames.ContainsKey($file.BaseName)) {
        Write-Host "Deleting matched file: $($file.Name)"
        Remove-Item -LiteralPath $file.FullName -Force
        $deletedCount++
    } else {
        Write-Host "Skipping unmatched file: $($file.Name)"
        $skippedCount++
    }
}

Write-Host "-----------------"
Write-Host "Done. Deleted: $deletedCount files, Skipped: $skippedCount files"
