$basePath = "C:\All phones data"
$momStorage = "$basePath\mom phone storage"
$momNewStorage = "$basePath\mom new one storage"
$extensions = @('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic', '.mp4', '.mov', '.avi', '.mkv', '.wmv')

Write-Host "Finding files in Mom Storage..."
$momFiles = Get-ChildItem -Path $momStorage -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $extensions -contains $_.Extension.ToLower() }

Write-Host "Finding files in Mom New Storage..."
$momNewFiles = Get-ChildItem -Path $momNewStorage -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $extensions -contains $_.Extension.ToLower() }

Write-Host "Finding ALL media files in C:\All phones data..."
$allFiles = Get-ChildItem -Path $basePath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $extensions -contains $_.Extension.ToLower() }

Write-Host "Optimizing hash calculation by grouping by size..."
$momSizeGroups = @{}
foreach ($file in $momFiles) {
    $sizeStr = $file.Length.ToString()
    if (-not $momSizeGroups.ContainsKey($sizeStr)) {
        $momSizeGroups[$sizeStr] = @()
    }
    $momSizeGroups[$sizeStr] += $file
}

$clonesToDelete = @()
foreach ($newFile in $momNewFiles) {
    $sizeStr = $newFile.Length.ToString()
    if ($momSizeGroups.ContainsKey($sizeStr)) {
        # Size matches! Now we hash.
        $newFileHash = (Get-FileHash -Path $newFile.FullName -Algorithm MD5).Hash
        $potentialMatches = $momSizeGroups[$sizeStr]
        
        foreach ($match in $potentialMatches) {
            $matchHash = (Get-FileHash -Path $match.FullName -Algorithm MD5).Hash
            if ($newFileHash -eq $matchHash) {
                $clonesToDelete += [PSCustomObject]@{
                    FileToDelete = $newFile.FullName
                    OriginalInMomStorage = $match.FullName
                    SizeMB = [math]::Round($newFile.Length / 1MB, 2)
                }
                break # Found the clone, no need to check other matches of same size
            }
        }
    }
}

# Export Clones
$clonesToDelete | Export-Csv -Path "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\clones_to_delete.csv" -NoTypeInformation

# Export All Files List
$allFilesList = $allFiles | Select-Object FullName, @{Name="SizeMB";Expression={[math]::Round($_.Length / 1MB, 2)}}, CreationTime, Extension
$allFilesList | Export-Csv -Path "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\all_media_files.csv" -NoTypeInformation

$summary = [PSCustomObject]@{
    TotalClonesFound = $clonesToDelete.Count
    TotalCloneSizeMB = [math]::Round(($clonesToDelete | Measure-Object SizeMB -Sum).Sum, 2)
    TotalMediaFiles = $allFiles.Count
}

$summary | ConvertTo-Json > "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\clone_summary.json"
Write-Host "Script completed successfully. Clones found: $($clonesToDelete.Count)"
