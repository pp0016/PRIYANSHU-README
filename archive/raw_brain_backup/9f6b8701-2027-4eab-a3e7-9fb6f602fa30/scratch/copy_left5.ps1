$destDir = "C:\Users\renu5\Videos\PP phones top all videos to give in Google Drive_Compressed\Left5"
$srcDir = "G:\My Drive\Pp another folder"

if (-not (Test-Path -LiteralPath $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

$filesToCopy = @(
    "VID20241127095543.mp4",
    "Record_2024-12-09-23-17-12_b864ea0b534de5941fd13c5c04397e2b.mp4",
    "Record_2025-06-08-00-23-34_a2ccbca8226e4060be63d52b28e3a3d7.mp4",
    "VID20240929134941.mp4",
    "VID20241027144908.mp4"
)

foreach ($file in $filesToCopy) {
    $srcPath = Join-Path -Path $srcDir -ChildPath $file
    $destPath = Join-Path -Path $destDir -ChildPath $file
    Write-Host "Copying $file..."
    Copy-Item -LiteralPath $srcPath -Destination $destPath -Force
}

Write-Host "All 5 files copied to Left5 folder successfully."
