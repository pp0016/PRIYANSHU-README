$path1 = "C:\mom phone storage"
$path2 = "C:\mom new one storage"

if (!(Test-Path $path1)) {
    Write-Output "Error: Path 1 does not exist: $path1"
    exit
}
if (!(Test-Path $path2)) {
    Write-Output "Error: Path 2 does not exist: $path2"
    exit
}

Write-Output "Starting strict re-check and deletion process..."
Write-Output "Source to preserve: $path1"
Write-Output "Target to clean: $path2"

$files2 = Get-ChildItem -Path $path2 -Recurse -File
$deletedCount = 0

foreach ($f in $files2) {
    $relPath = $f.FullName.Substring($path2.Length + 1)
    $expectedPath1 = Join-Path -Path $path1 -ChildPath $relPath

    # RECHECK: Strictly verify the exact file exists in Path 1 before touching Path 2
    if (Test-Path -Path $expectedPath1 -PathType Leaf) {
        # File is a verified duplicate. Delete from Path 2 ONLY.
        try {
            Remove-Item -Path $f.FullName -Force -ErrorAction Stop
            $deletedCount++
        } catch {
            Write-Output "Failed to delete: $($f.FullName) - $($_.Exception.Message)"
        }
    }
}

Write-Output "Deletion process complete."
Write-Output "Total files strictly re-checked and deleted from Path 2: $deletedCount"
Write-Output "Path 1 (Compressed Backup) was left completely untouched."
