$sourceDir = "C:\Users\renu5\Downloads\New folder\Instagram"
$destDir = "C:\Users\renu5\Downloads\New folder\Instagram compressed"

$destFiles = Get-ChildItem -Path $destDir -File
if ($destFiles.Count -gt 0) {
    foreach ($file in $destFiles) {
        if ((New-TimeSpan -Start $file.LastWriteTime -End (Get-Date)).TotalMinutes -lt 5) {
            Write-Host "Removing recently modified potentially partial file: $($file.Name)"
            Remove-Item $file.FullName -Force -ErrorAction SilentlyContinue
        }
    }
}

$sourceFiles = Get-ChildItem -Path $sourceDir -File
$destFiles = Get-ChildItem -Path $destDir -File

$destNames = $destFiles | Select-Object -ExpandProperty Name
$remainingFiles = $sourceFiles | Where-Object { $destNames -notcontains $_.Name }

Write-Host "Remaining files to process: $($remainingFiles.Count)"

$pool = [runspacefactory]::CreateRunspacePool(1, 5)
$pool.Open()
$jobs = @()

foreach ($file in $remainingFiles) {
    $ps = [PowerShell]::Create()
    $ps.RunspacePool = $pool
    
    $script = {
        param($filePath, $destDir)
        
        $file = Get-Item $filePath
        $outPath = Join-Path $destDir $file.Name
        $ext = $file.Extension.ToLower()
        
        $attempt = 0
        $maxAttempts = 3
        $success = $false
        
        while ($attempt -lt $maxAttempts -and -not $success) {
            $attempt++
            if ($ext -match "\.(mp4|mov|avi|mkv)$") {
                $ffmpegArgs = "-i `"$($file.FullName)`" -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k -y `"$outPath`""
                $p = Start-Process -FilePath "ffmpeg" -ArgumentList $ffmpegArgs -NoNewWindow -Wait -PassThru
            } elseif ($ext -match "\.(jpg|jpeg|png|heic|webp)$") {
                $ffmpegArgs = "-i `"$($file.FullName)`" -q:v 5 -y `"$outPath`""
                $p = Start-Process -FilePath "ffmpeg" -ArgumentList $ffmpegArgs -NoNewWindow -Wait -PassThru
            } else {
                Copy-Item -Path $file.FullName -Destination $outPath -Force
                $success = $true
                break
            }
            
            if (Test-Path $outPath) {
                $outFile = Get-Item $outPath
                if ($outFile.Length -gt 0) {
                    $success = $true
                } else {
                    Remove-Item $outPath -Force
                }
            }
        }
        
        return [PSCustomObject]@{
            Name = $file.Name
            Success = $success
        }
    }
    
    $ps.AddScript($script).AddArgument($file.FullName).AddArgument($destDir) | Out-Null
    $jobs += [PSCustomObject]@{
        PowerShell = $ps
        Handle = $ps.BeginInvoke()
    }
}

$successCount = 0
$failCount = 0

foreach ($job in $jobs) {
    $result = $job.PowerShell.EndInvoke($job.Handle)
    if ($result.Success) {
        $successCount++
    } else {
        $failCount++
    }
    $job.PowerShell.Dispose()
}

$pool.Close()
$pool.Dispose()

$finalSourceFiles = Get-ChildItem -Path $sourceDir -File
$finalDestFiles = Get-ChildItem -Path $destDir -File

$origSize = ($finalSourceFiles | Measure-Object -Property Length -Sum).Sum
$newSize = ($finalDestFiles | Measure-Object -Property Length -Sum).Sum
$saved = $origSize - $newSize

Write-Host "--- SUMMARY ---"
Write-Host "Original Size: $origSize"
Write-Host "New Size: $newSize"
Write-Host "Space Saved: $saved"
Write-Host "Success: $successCount"
Write-Host "Failed: $failCount"
Write-Host "Total Successfully in Dest: $($finalDestFiles.Count)"
