$files = Get-ChildItem -Path 'C:\mom phone storage' -File -Recurse | Where-Object { $_.Length -ge 1MB } | Sort-Object Length -Descending

$totalCount = $files.Count
if ($totalCount -eq 0) {
    Write-Host '{"error": "No files over 1MB found"}'
    exit
}

$totalSize = ($files | Measure-Object -Property Length -Sum).Sum
$top20PercentCount = [math]::Round($totalCount * 0.2)
if ($top20PercentCount -eq 0 -and $totalCount -gt 0) { $top20PercentCount = 1 }

$top20Files = $files | Select-Object -First $top20PercentCount
$top20Size = ($top20Files | Measure-Object -Property Length -Sum).Sum

$videos = $top20Files | Where-Object { $_.Extension -match '\.(mp4|mov|avi|mkv)$' }
$images = $top20Files | Where-Object { $_.Extension -match '\.(jpg|jpeg|png|heic)$' }

[PSCustomObject]@{
    TotalFilesOver1MB = $totalCount
    TotalSizeGB = [math]::Round($totalSize / 1GB, 2)
    Top20PercentCount = $top20PercentCount
    Top20SizeGB = [math]::Round($top20Size / 1GB, 2)
    PercentageOfTotalSize = [math]::Round(($top20Size / $totalSize) * 100, 2)
    Top20VideosCount = @($videos).Count
    Top20ImagesCount = @($images).Count
} | ConvertTo-Json
