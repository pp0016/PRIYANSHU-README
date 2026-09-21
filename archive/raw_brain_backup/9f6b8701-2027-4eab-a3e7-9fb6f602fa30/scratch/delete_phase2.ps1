$localFolder = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\1 In Education with Toddlers"
$gDriveFolder = "G:\My Drive\My top five most storage size videos\PP phones top 100 videos to give in Google Drive"

$localFiles = Get-ChildItem -Path $localFolder -File
$gDriveFiles = Get-ChildItem -Path $gDriveFolder -File

$localBaseNames = @{}
foreach ($file in $localFiles) {
    $localBaseNames[$file.BaseName] = $true
}

$deletedCount = 0

foreach ($file in $gDriveFiles) {
    if ($localBaseNames.ContainsKey($file.BaseName)) {
        Remove-Item -LiteralPath $file.FullName -Force
        $deletedCount++
    }
}
Write-Host "Finished deleting $deletedCount files."
