$root = "C:\Users\renu5\Downloads\Takeout"
$videos = Get-ChildItem -Path $root -Recurse -File -Filter '*.mp4' | Sort-Object Length -Descending

$totalSize = ($videos | Measure-Object -Property Length -Sum).Sum
$totalGB = [math]::Round($totalSize / 1GB, 2)
$totalCount = $videos.Count

Write-Host "=== VIDEO SIZE DISTRIBUTION (Total: $totalCount files, $totalGB GB) ==="
Write-Host ""

# Top 20 largest
Write-Host "--- TOP 20 LARGEST VIDEOS ---"
$runningSum = 0
$videos | Select-Object -First 20 | ForEach-Object {
    $sizeMB = [math]::Round($_.Length / 1MB, 1)
    $runningSum += $_.Length
    $cumPct = [math]::Round(($runningSum / $totalSize) * 100, 1)
    Write-Host "$sizeMB MB | cumulative: $cumPct% | $($_.Name)"
}

Write-Host ""
Write-Host "--- PARETO BREAKDOWN ---"

# How many videos make up 50%, 60%, 70%, 80%, 90% of storage
foreach ($threshold in @(50, 60, 70, 80, 90, 95)) {
    $targetBytes = $totalSize * ($threshold / 100)
    $cumSum = 0
    $count = 0
    foreach ($v in $videos) {
        $cumSum += $v.Length
        $count++
        if ($cumSum -ge $targetBytes) { break }
    }
    $cumGB = [math]::Round($cumSum / 1GB, 2)
    Write-Host "$threshold% of storage ($cumGB GB) = top $count videos (out of $totalCount)"
}

Write-Host ""
Write-Host "--- SIZE BUCKETS ---"
$buckets = @(
    @{Label="200-400 MB"; Min=200MB; Max=400MB},
    @{Label="100-200 MB"; Min=100MB; Max=200MB},
    @{Label="50-100 MB"; Min=50MB; Max=100MB},
    @{Label="20-50 MB"; Min=20MB; Max=50MB},
    @{Label="10-20 MB"; Min=10MB; Max=20MB},
    @{Label="5-10 MB"; Min=5MB; Max=10MB},
    @{Label="1-5 MB"; Min=1MB; Max=5MB},
    @{Label="Under 1 MB"; Min=0; Max=1MB}
)

foreach ($b in $buckets) {
    $bucket = $videos | Where-Object { $_.Length -ge $b.Min -and $_.Length -lt $b.Max }
    $bCount = ($bucket | Measure-Object).Count
    $bSizeMB = [math]::Round(($bucket | Measure-Object -Property Length -Sum).Sum / 1MB, 1)
    $bPct = if ($totalSize -gt 0) { [math]::Round(($bucket | Measure-Object -Property Length -Sum).Sum / $totalSize * 100, 1) } else { 0 }
    if ($bCount -gt 0) {
        Write-Host "$($b.Label): $bCount files, $bSizeMB MB ($bPct% of total)"
    }
}
