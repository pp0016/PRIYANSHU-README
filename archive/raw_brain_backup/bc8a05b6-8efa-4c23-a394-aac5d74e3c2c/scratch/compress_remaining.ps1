$sourceDir = "C:\Users\renu5\Downloads\New folder\Instagram"
$destDir = "C:\Users\renu5\Downloads\New folder\Instagram compressed"

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

$files = Get-ChildItem -Path $sourceDir -File

$scriptBlock = {
    param($file, $destDir)
    
    $destFile = Join-Path $destDir $file.Name
    if (Test-Path $destFile) {
        if ((Get-Item $destFile).Length -gt 0) {
            return [pscustomobject]@{ Name = $file.Name; Status = "Skipped" }
        }
    }
    
    $ext = $file.Extension.ToLower()
    $isVideo = $ext -match "\.(mp4|mov|mkv|avi|webm)$"
    $isImage = $ext -match "\.(jpg|jpeg|png|webp|heic)$"
    
    if (-not $isVideo -and -not $isImage) {
        return [pscustomobject]@{ Name = $file.Name; Status = "Skipped" }
    }
    
    $success = $false
    for ($i = 0; $i -lt 3; $i++) {
        if ($isVideo) {
            $cmd = "ffmpeg -y -i `"$($file.FullName)`" -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k `"$destFile`" 2>&1"
        } else {
            $cmd = "ffmpeg -y -i `"$($file.FullName)`" -q:v 5 `"$destFile`" 2>&1"
        }
        
        $output = Invoke-Expression $cmd
        
        if (Test-Path $destFile) {
            $size = (Get-Item $destFile).Length
            if ($size -gt 0) {
                $success = $true
                break
            } else {
                Remove-Item $destFile -Force
            }
        }
    }
    
    if ($success) {
        return [pscustomobject]@{ Name = $file.Name; Status = "Success" }
    } else {
        return [pscustomobject]@{ Name = $file.Name; Status = "Failed" }
    }
}

$pool = [runspacefactory]::CreateRunspacePool(1, 5)
$pool.Open()

$jobs = @()
foreach ($file in $files) {
    $ps = [powershell]::Create().AddScript($scriptBlock).AddArgument($file).AddArgument($destDir)
    $ps.RunspacePool = $pool
    $jobs += [pscustomobject]@{
        PowerShell = $ps
        Handle = $ps.BeginInvoke()
    }
}

$results = @()
foreach ($job in $jobs) {
    $results += $job.PowerShell.EndInvoke($job.Handle)
    $job.PowerShell.Dispose()
}

$pool.Close()
$pool.Dispose()

$results | Export-Csv -Path (Join-Path $destDir "compression_results.csv") -NoTypeInformation

$successCount = ($results | Where-Object { $_.Status -eq 'Success' }).Count
$failedCount = ($results | Where-Object { $_.Status -eq 'Failed' }).Count
$skippedCount = ($results | Where-Object { $_.Status -eq 'Skipped' }).Count

$totalFiles = $files.Count
$totalDestFiles = (Get-ChildItem -Path $destDir -File | Where-Object { $_.Name -ne "compression_results.csv" }).Count

Write-Host "Total original files: $totalFiles"
Write-Host "Total compressed files currently: $totalDestFiles"
Write-Host "Success this run: $successCount"
Write-Host "Failed this run: $failedCount"
Write-Host "Skipped this run: $skippedCount"

$origSize = (Get-ChildItem -Path $sourceDir -File | Measure-Object -Property Length -Sum).Sum
$newSize = (Get-ChildItem -Path $destDir -File | Where-Object { $_.Name -ne "compression_results.csv" } | Measure-Object -Property Length -Sum).Sum
Write-Host "Original Size: $origSize"
Write-Host "New Size: $newSize"
