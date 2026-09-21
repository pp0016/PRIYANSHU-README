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

# Just do a small batch test run to prove the concept without scanning everything if it's huge, 
# or scan all and just output a 5% sample. Given we want to find actual matches, 
# scanning all in memory is fast enough for a dry run, but we will limit output.

$files1 = Get-ChildItem -Path $path1 -Recurse -File
$files2 = Get-ChildItem -Path $path2 -Recurse -File

$hash1 = @{}
foreach ($f in $files1) {
    # Using relative path from base folder
    $relPath = $f.FullName.Substring($path1.Length + 1)
    $hash1[$relPath] = $f
}

$hash2 = @{}
foreach ($f in $files2) {
    $relPath = $f.FullName.Substring($path2.Length + 1)
    $hash2[$relPath] = $f
}

$duplicates = @()
$onlyInPath1 = @()
$onlyInPath2 = @()

foreach ($key in $hash1.Keys) {
    if ($hash2.ContainsKey($key)) {
        $duplicates += $key
    } else {
        $onlyInPath1 += $key
    }
}

foreach ($key in $hash2.Keys) {
    if (-not $hash1.ContainsKey($key)) {
        $onlyInPath2 += $key
    }
}

Write-Output "=== TEST RUN RESULTS ==="
Write-Output "Total Files in Path 1 (Compressed Backup): $($files1.Count)"
Write-Output "Total Files in Path 2 (New Backup): $($files2.Count)"
Write-Output ""
Write-Output "Category 1: Safe to delete in bulk (Duplicates): $($duplicates.Count)"
Write-Output "Sample:"
$duplicates | Select-Object -First 5 | ForEach-Object { Write-Output " - $_" }

Write-Output ""
Write-Output "Category 2: Must remain constant (Only in Path 1): $($onlyInPath1.Count)"
Write-Output "Sample:"
$onlyInPath1 | Select-Object -First 5 | ForEach-Object { Write-Output " - $_" }

Write-Output ""
Write-Output "Category 3: Brand new in Path 2 (Do not delete): $($onlyInPath2.Count)"
Write-Output "Sample:"
$onlyInPath2 | Select-Object -First 5 | ForEach-Object { Write-Output " - $_" }
