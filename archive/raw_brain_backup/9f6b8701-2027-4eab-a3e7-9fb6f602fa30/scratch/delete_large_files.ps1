$sourceGDriveFolder = "G:\My Drive\My top five most storage size videos"

$filesToDelete = @(
    "Record_2024-01-21-20-38-06.mp4",
    "Record_2025-01-22-20-49-21.mp4"
)

$deletedCount = 0
foreach ($file in $filesToDelete) {
    $filePath = Join-Path -Path $sourceGDriveFolder -ChildPath $file
    if (Test-Path -LiteralPath $filePath) {
        Remove-Item -LiteralPath $filePath -Force
        $deletedCount++
    }
}
Write-Host "Deleted $deletedCount large files from Google Drive."
