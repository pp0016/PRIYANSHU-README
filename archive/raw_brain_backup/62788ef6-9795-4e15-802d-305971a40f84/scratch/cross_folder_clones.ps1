$folders = @{
    "MomNew" = "C:\All phones data\mom new one storage"
    "Mom" = "C:\All phones data\mom phone storage"
    "PP" = "C:\All phones data\PP phones top all videos to give in Google Drive_Compressed"
}

$imageExts = @('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.heic')
$videoExts = @('.mp4', '.mov', '.avi', '.mkv', '.wmv')
$allExts = $imageExts + $videoExts

$allFiles = @()

foreach ($key in $folders.Keys) {
    $path = $folders[$key]
    Write-Host "Scanning $key..."
    $files = Get-ChildItem -Path $path -Recurse -File -ErrorAction SilentlyContinue | Where-Object { $allExts -contains $_.Extension.ToLower() }
    
    foreach ($file in $files) {
        $type = if ($imageExts -contains $file.Extension.ToLower()) { "Image" } else { "Video" }
        $allFiles += [PSCustomObject]@{
            RootFolder = $key
            Type = $type
            File = $file
            Length = $file.Length
            Path = $file.FullName
        }
    }
}

Write-Host "Grouping by Size..."
$sizeGroups = $allFiles | Group-Object Length | Where-Object { $_.Count -gt 1 }

$crossClones = @()
$stats = @{
    ImageClones = 0
    VideoClones = 0
    ImageWastedSize = 0
    VideoWastedSize = 0
}

Write-Host "Hashing potential cross-folder clones..."
foreach ($group in $sizeGroups) {
    # Check if files in this size group come from more than 1 distinct root folder
    $distinctRoots = $group.Group | Select-Object -ExpandProperty RootFolder -Unique
    if ($distinctRoots.Count -gt 1) {
        # Calculate hashes
        $hashGroups = $group.Group | Group-Object { (Get-FileHash -Path $_.Path -Algorithm MD5).Hash } | Where-Object { $_.Count -gt 1 }
        
        foreach ($hGroup in $hashGroups) {
            $hDistinctRoots = $hGroup.Group | Select-Object -ExpandProperty RootFolder -Unique
            if ($hDistinctRoots.Count -gt 1) {
                # It is a cross-folder clone!
                # We count all files after the first one as "wasted" clones
                # Wait, if there's 1 in Mom, 1 in PP, 1 in MomNew -> 3 files total, 2 are wasted clones.
                $type = $hGroup.Group[0].Type
                $fileSize = $hGroup.Group[0].Length
                $wastedCount = $hGroup.Count - 1
                $wastedBytes = $wastedCount * $fileSize
                
                if ($type -eq "Image") {
                    $stats.ImageClones += $wastedCount
                    $stats.ImageWastedSize += $wastedBytes
                } else {
                    $stats.VideoClones += $wastedCount
                    $stats.VideoWastedSize += $wastedBytes
                }
                
                $crossClones += [PSCustomObject]@{
                    Hash = $hGroup.Name
                    Type = $type
                    SizeMB = [math]::Round($fileSize / 1MB, 2)
                    Count = $hGroup.Count
                    Locations = ($hGroup.Group | Select-Object -ExpandProperty Path) -join " | "
                }
            }
        }
    }
}

$summary = [PSCustomObject]@{
    TotalImageClones = $stats.ImageClones
    TotalVideoClones = $stats.VideoClones
    TotalImageWastedMB = [math]::Round($stats.ImageWastedSize / 1MB, 2)
    TotalVideoWastedMB = [math]::Round($stats.VideoWastedSize / 1MB, 2)
    TotalWastedMB = [math]::Round(($stats.ImageWastedSize + $stats.VideoWastedSize) / 1MB, 2)
}

$summary | ConvertTo-Json > "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\cross_folder_summary.json"
$crossClones | Export-Csv -Path "C:\Users\renu5\.gemini\antigravity\brain\62788ef6-9795-4e15-802d-305971a40f84\scratch\cross_folder_clones.csv" -NoTypeInformation

Write-Host "Done!"
