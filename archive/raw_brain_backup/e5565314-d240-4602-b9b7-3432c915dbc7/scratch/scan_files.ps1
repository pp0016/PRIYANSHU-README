$target = 'C:\mom phone storage'
if (-Not (Test-Path $target)) {
    Write-Output "Directory '$target' does not exist."
    exit 1
}

$files = @(Get-ChildItem -Path $target -Recurse -File)
$zeroByteFiles = @($files | Where-Object { $_.Length -eq 0 })
$smallFiles = @($files | Where-Object { $_.Length -gt 0 -and $_.Length -lt 1024 })

Write-Output "=== Scan Results for $target ==="
Write-Output "Total Files Scanned: $($files.Count)"
Write-Output ""
Write-Output "--- Zero Byte Files ---"
if ($zeroByteFiles.Count -gt 0) {
    $zeroByteFiles | Select-Object FullName | Format-List
} else {
    Write-Output "No zero-byte files found."
}

Write-Output ""
Write-Output "--- Files Under 1KB ---"
if ($smallFiles.Count -gt 0) {
    $smallFiles | Select-Object FullName, Length | Format-Table -AutoSize
} else {
    Write-Output "No files under 1KB found."
}
