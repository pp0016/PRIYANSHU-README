$sourceGDriveFolder = "G:\My Drive\My top five most storage size videos"
$destParent = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\Left5"
$destFolder = Join-Path -Path $destParent -ChildPath "Education with Toddlers Big Files"

if (-not (Test-Path -LiteralPath $destFolder)) {
    New-Item -ItemType Directory -Path $destFolder | Out-Null
}

$filesToCopy = @(
    "Record_2024-01-21-20-38-06.mp4",
    "Record_2025-01-22-20-49-21.mp4"
)

foreach ($file in $filesToCopy) {
    $sourcePath = Join-Path -Path $sourceGDriveFolder -ChildPath $file
    $destPath = Join-Path -Path $destFolder -ChildPath $file
    
    if (Test-Path -LiteralPath $sourcePath) {
        Write-Host "Copying $file ..."
        Copy-Item -LiteralPath $sourcePath -Destination $destPath -Force
        Write-Host "Done copying $file."
    } else {
        Write-Host "Error: Could not find $file in Google Drive."
    }
}
Write-Host "All files copied successfully."
