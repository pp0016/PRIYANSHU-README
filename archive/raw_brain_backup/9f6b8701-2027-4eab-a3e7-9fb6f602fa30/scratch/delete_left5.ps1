$gDriveFolder = "G:\My Drive\Pp another folder"

$filesToDelete = @(
    "VID20241127095543.mp4",
    "Record_2024-12-09-23-17-12_b864ea0b534de5941fd13c5c04397e2b.mp4",
    "Record_2025-06-08-00-23-34_a2ccbca8226e4060be63d52b28e3a3d7.mp4",
    "VID20240929134941.mp4",
    "VID20241027144908.mp4"
)

foreach ($file in $filesToDelete) {
    $filePath = Join-Path -Path $gDriveFolder -ChildPath $file
    if (Test-Path -LiteralPath $filePath) {
        Write-Host "Deleting $file from Google Drive..."
        Remove-Item -LiteralPath $filePath -Force
    } else {
        Write-Host "File $file not found in Google Drive."
    }
}
Write-Host "Finished deleting the 5 files from Google Drive."
