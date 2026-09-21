$oldDir = "C:\mom phone storage"
$newDir = "C:\mom new one storage"

Write-Host "Scanning $oldDir..."
$oldFiles = Get-ChildItem -Path $oldDir -Recurse -File | Select-Object -Property @{Name='RelativePath'; Expression={$_.FullName.Substring($oldDir.Length + 1)}}

Write-Host "Scanning $newDir..."
$newFiles = Get-ChildItem -Path $newDir -Recurse -File | Select-Object -Property @{Name='RelativePath'; Expression={$_.FullName.Substring($newDir.Length + 1)}}, Length

$oldSet = New-Object System.Collections.Generic.HashSet[string]
foreach ($f in $oldFiles) { [void]$oldSet.Add($f.RelativePath.ToLower()) }

$newSet = New-Object System.Collections.Generic.HashSet[string]
foreach ($f in $newFiles) { [void]$newSet.Add($f.RelativePath.ToLower()) }

$inBoth = 0
$onlyInNew = 0
$onlyInOld = 0
$newFileSizeTotal = 0

foreach ($f in $newFiles) {
    if ($oldSet.Contains($f.RelativePath.ToLower())) {
        $inBoth++
    } else {
        $onlyInNew++
        $newFileSizeTotal += $f.Length
    }
}

foreach ($f in $oldFiles) {
    if (-not $newSet.Contains($f.RelativePath.ToLower())) {
        $onlyInOld++
    }
}

$newFileSizeGB = [math]::Round($newFileSizeTotal / 1GB, 2)

Write-Host ""
Write-Host "=== COMPARISON RESULTS ==="
Write-Host "Total Files in Compressed Backup ($oldDir): $($oldFiles.Count)"
Write-Host "Total Files in New Backup ($newDir): $($newFiles.Count)"
Write-Host "--------------------------------"
Write-Host "Files in BOTH (Duplicates): $inBoth"
Write-Host "Files ONLY in New Backup (New stuff to keep): $onlyInNew (Total Size: $newFileSizeGB GB)"
Write-Host "Files ONLY in Old Backup: $onlyInOld"
Write-Host "=========================="
