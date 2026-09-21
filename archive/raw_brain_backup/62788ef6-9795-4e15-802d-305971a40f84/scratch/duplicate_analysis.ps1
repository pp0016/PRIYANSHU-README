$targetPath = "C:\All phones data"
$extensions = @('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic', '.mp4', '.mov', '.avi', '.mkv', '.wmv')

Write-Host "Getting all files..."
$files = Get-ChildItem -Path $targetPath -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $extensions -contains $_.Extension.ToLower() }

Write-Host "Found $($files.Count) media files."

# 1. Analyze by Name
Write-Host "Analyzing by Name..."
$nameGroups = $files | Group-Object Name | Where-Object { $_.Count -gt 1 }
$sameNameCount = 0
$sameNameWaste = 0
$topNameGroups = @()

foreach ($group in $nameGroups | Sort-Object Count -Descending) {
    $sameNameCount += ($group.Count - 1)
    
    # Sort files in group by size descending, keep the first (largest) as original, rest are "waste"
    $sortedFiles = $group.Group | Sort-Object Length -Descending
    $wasteInGroup = 0
    for ($i = 1; $i -lt $sortedFiles.Count; $i++) {
        $wasteInGroup += $sortedFiles[$i].Length
    }
    $sameNameWaste += $wasteInGroup
    
    if ($topNameGroups.Count -lt 10) {
        $topNameGroups += [PSCustomObject]@{
            Name = $group.Name
            Count = $group.Count
            TotalSizeMB = [math]::Round(($group.Group | Measure-Object Length -Sum).Sum / 1MB, 2)
            Paths = $group.Group.FullName
        }
    }
}

# 2. Analyze by True Duplicate (Same Hash)
Write-Host "Analyzing by Content (Size & Hash)..."
$sizeGroups = $files | Group-Object Length | Where-Object { $_.Count -gt 1 }
$exactDuplicatesCount = 0
$exactDuplicatesWaste = 0
$topExactDuplicates = @()

foreach ($sizeGroup in $sizeGroups) {
    # Calculate hash only for files with same size
    $hashGroups = $sizeGroup.Group | Get-FileHash -Algorithm MD5 | Group-Object Hash | Where-Object { $_.Count -gt 1 }
    
    foreach ($hashGroup in $hashGroups) {
        $exactDuplicatesCount += ($hashGroup.Count - 1)
        # Size of one file in this group
        $fileSize = (Get-Item $hashGroup.Group[0].Path).Length
        $exactDuplicatesWaste += ($fileSize * ($hashGroup.Count - 1))
        
        $topExactDuplicates += [PSCustomObject]@{
            Hash = $hashGroup.Name
            Count = $hashGroup.Count
            SizeMB = [math]::Round($fileSize / 1MB, 2)
            WastedMB = [math]::Round(($fileSize * ($hashGroup.Count - 1)) / 1MB, 2)
            Paths = $hashGroup.Group.Path
        }
    }
}

$topExactDuplicates = $topExactDuplicates | Sort-Object WastedMB -Descending | Select-Object -First 10

# Prepare JSON output
$result = [PSCustomObject]@{
    TotalMediaFiles = $files.Count
    TotalMediaSizeMB = [math]::Round(($files | Measure-Object Length -Sum).Sum / 1MB, 2)
    SameNameStats = [PSCustomObject]@{
        FilesWithSameName = $sameNameCount
        EstimatedWastedSizeMB = [math]::Round($sameNameWaste / 1MB, 2)
        TopGroups = $topNameGroups
    }
    ExactDuplicateStats = [PSCustomObject]@{
        ExactDuplicateFiles = $exactDuplicatesCount
        ExactWastedSizeMB = [math]::Round($exactDuplicatesWaste / 1MB, 2)
        TopDuplicates = $topExactDuplicates
    }
}

$result | ConvertTo-Json -Depth 5 > "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\duplicate_analysis_result.json"
Write-Host "Analysis complete. Results saved to JSON."
