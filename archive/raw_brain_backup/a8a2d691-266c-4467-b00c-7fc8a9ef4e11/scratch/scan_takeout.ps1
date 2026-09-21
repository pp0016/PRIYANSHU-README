$root = "C:\Users\renu5\Downloads\Takeout"

# Video extensions
$vidExt = @('.mp4','.avi','.mkv','.mov','.wmv','.flv','.webm','.3gp','.m4v','.mpg','.mpeg')
# Image extensions  
$imgExt = @('.jpg','.jpeg','.png','.bmp','.tiff','.tif','.webp','.heic','.heif','.gif')

$allFiles = Get-ChildItem -Path $root -Recurse -File

$videos = $allFiles | Where-Object { $vidExt -contains $_.Extension.ToLower() }
$images = $allFiles | Where-Object { $imgExt -contains $_.Extension.ToLower() }
$jsonFiles = $allFiles | Where-Object { $_.Extension.ToLower() -eq '.json' }
$otherFiles = $allFiles | Where-Object { $vidExt -notcontains $_.Extension.ToLower() -and $imgExt -notcontains $_.Extension.ToLower() -and $_.Extension.ToLower() -ne '.json' }

Write-Host "=== TAKEOUT SCAN RESULTS ==="
Write-Host ""

# Videos
$vidCount = ($videos | Measure-Object).Count
$vidSizeGB = [math]::Round(($videos | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
Write-Host "VIDEOS: $vidCount files, $vidSizeGB GB total"

# Large videos (>400MB)
$largeVids = $videos | Where-Object { $_.Length -gt 400MB }
$largeCount = ($largeVids | Measure-Object).Count
Write-Host "  Large videos (>400MB): $largeCount files"
if ($largeCount -gt 0) {
    $largeVids | Sort-Object Length -Descending | ForEach-Object {
        $sizeMB = [math]::Round($_.Length / 1MB, 1)
        Write-Host "    $sizeMB MB - $($_.Name)"
    }
}

# Medium videos (50-400MB)
$medVids = $videos | Where-Object { $_.Length -gt 50MB -and $_.Length -le 400MB }
$medCount = ($medVids | Measure-Object).Count
$medSizeGB = [math]::Round(($medVids | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
Write-Host "  Medium videos (50-400MB): $medCount files, $medSizeGB GB"

# Small videos (<50MB)
$smallVids = $videos | Where-Object { $_.Length -le 50MB }
$smallCount = ($smallVids | Measure-Object).Count
$smallSizeMB = [math]::Round(($smallVids | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
Write-Host "  Small videos (<50MB): $smallCount files, $smallSizeMB MB"

Write-Host ""

# Images
$imgCount = ($images | Measure-Object).Count
$imgSizeGB = [math]::Round(($images | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
Write-Host "IMAGES: $imgCount files, $imgSizeGB GB total"

# Image format breakdown
$images | Group-Object { $_.Extension.ToLower() } | Sort-Object Count -Descending | ForEach-Object {
    $extSizeMB = [math]::Round(($_.Group | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
    Write-Host "  $($_.Name): $($_.Count) files, $extSizeMB MB"
}

Write-Host ""

# JSON metadata files
$jsonCount = ($jsonFiles | Measure-Object).Count
$jsonSizeMB = [math]::Round(($jsonFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
Write-Host "JSON METADATA: $jsonCount files, $jsonSizeMB MB"

Write-Host ""

# Other files
$otherCount = ($otherFiles | Measure-Object).Count
if ($otherCount -gt 0) {
    $otherSizeMB = [math]::Round(($otherFiles | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
    Write-Host "OTHER FILES: $otherCount files, $otherSizeMB MB"
    $otherFiles | Group-Object { $_.Extension.ToLower() } | Sort-Object Count -Descending | ForEach-Object {
        Write-Host "  $($_.Name): $($_.Count) files"
    }
}

Write-Host ""
$totalSizeGB = [math]::Round(($allFiles | Measure-Object -Property Length -Sum).Sum / 1GB, 2)
Write-Host "TOTAL: $($allFiles.Count) files, $totalSizeGB GB"

# Video format breakdown
Write-Host ""
Write-Host "VIDEO FORMAT BREAKDOWN:"
$videos | Group-Object { $_.Extension.ToLower() } | Sort-Object @{E={($_.Group | Measure-Object -Property Length -Sum).Sum}} -Descending | ForEach-Object {
    $extSizeMB = [math]::Round(($_.Group | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
    Write-Host "  $($_.Name): $($_.Count) files, $extSizeMB MB"
}
