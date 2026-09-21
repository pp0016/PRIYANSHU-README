$InputDir = "C:\Users\renu5\Downloads\New folder\Instagram"
$OutputDir = "C:\Users\renu5\Downloads\New folder\Instagram compressed"
$MaxThreads = 8

if (-not (Test-Path $OutputDir)) {
    New-Item -ItemType Directory -Path $OutputDir | Out-Null
}

$files = Get-ChildItem -Path $InputDir -File -Recurse | Sort-Object Name | Select-Object -First 237

$OriginalSize = ($files | Measure-Object -Property Length -Sum).Sum

$ScriptBlock = {
    param($file, $OutputDir, $InputDir)

    $relPath = $file.FullName.Substring($InputDir.Length + 1)
    $outPath = Join-Path $OutputDir $relPath
    $outDir = Split-Path $outPath -Parent

    if (-not (Test-Path $outDir)) {
        $null = New-Item -ItemType Directory -Path $outDir -Force
    }

    # Check if already done and valid
    if ((Test-Path $outPath) -and ((Get-Item $outPath).Length -gt 0)) {
        $finalSize = (Get-Item $outPath).Length
        return [pscustomobject]@{ File = $file.FullName; Status = 'Skipped'; FinalSize = $finalSize }
    }

    $ext = $file.Extension.ToLower()
    $videoExts = @('.mp4', '.mov', '.mkv', '.avi', '.wmv', '.flv', '.webm', '.m4v', '.ts')
    $imageExts = @('.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.webp', '.heic')

    $success = $false
    for ($i = 0; $i -lt 3; $i++) {
        if ($ext -in $videoExts) {
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-y", "-i", "`"$($file.FullName)`"", "-c:v", "libx264", "-crf", "28", "-preset", "fast", "-c:a", "aac", "-b:a", "128k", "`"$outPath`"" -Wait -NoNewWindow -PassThru
        } elseif ($ext -in $imageExts) {
            $process = Start-Process -FilePath "ffmpeg" -ArgumentList "-y", "-i", "`"$($file.FullName)`"", "-q:v", "5", "`"$outPath`"" -Wait -NoNewWindow -PassThru
        } else {
            Copy-Item -Path $file.FullName -Destination $outPath -Force
            if (Test-Path $outPath) {
                return [pscustomobject]@{ File = $file.FullName; Status = 'Copied'; FinalSize = (Get-Item $outPath).Length }
            }
        }

        if (($process -ne $null -and $process.ExitCode -eq 0) -or ($process -eq $null)) {
            if ((Test-Path $outPath) -and ((Get-Item $outPath).Length -gt 0)) {
                $success = $true
                break
            }
        }
        
        # Failed or 0-byte file
        if (Test-Path $outPath) { Remove-Item $outPath -Force }
        Start-Sleep -Seconds 2
    }

    if ($success) {
        return [pscustomobject]@{ File = $file.FullName; Status = 'Success'; FinalSize = (Get-Item $outPath).Length }
    } else {
        return [pscustomobject]@{ File = $file.FullName; Status = 'Failed'; FinalSize = 0 }
    }
}

$RunspacePool = [runspacefactory]::CreateRunspacePool(1, $MaxThreads)
$RunspacePool.Open()
$Jobs = @()

foreach ($file in $files) {
    $PowerShell = [powershell]::Create().AddScript($ScriptBlock).AddArgument($file).AddArgument($OutputDir).AddArgument($InputDir)
    $PowerShell.RunspacePool = $RunspacePool
    $Jobs += [pscustomobject]@{
        Pipe = $PowerShell
        Status = $PowerShell.BeginInvoke()
    }
}

$Results = @()
foreach ($Job in $Jobs) {
    $Results += $Job.Pipe.EndInvoke($Job.Status)
    $Job.Pipe.Dispose()
}

$RunspacePool.Close()
$RunspacePool.Dispose()

$Results | Export-Csv -Path "C:\Users\renu5\.gemini\antigravity\brain\72ef2a62-cda5-49a3-9470-880557e03efe\scratch\compression_results_half.csv" -NoTypeInformation

$NewSize = ($Results | Measure-Object -Property FinalSize -Sum).Sum

$summary = @{
    OriginalSize = $OriginalSize
    NewSize = $NewSize
    SpaceSaved = ($OriginalSize - $NewSize)
    SuccessCount = ($Results | Where-Object { $_.Status -in @('Success', 'Skipped', 'Copied') } | Measure-Object).Count
    FailCount = ($Results | Where-Object { $_.Status -eq 'Failed' } | Measure-Object).Count
}

$summary | ConvertTo-Json | Out-File -FilePath "C:\Users\renu5\.gemini\antigravity\brain\72ef2a62-cda5-49a3-9470-880557e03efe\scratch\compression_summary_half.json"
