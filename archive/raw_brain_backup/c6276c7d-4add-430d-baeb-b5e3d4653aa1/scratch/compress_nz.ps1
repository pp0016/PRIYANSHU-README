$sourceDir = "C:\Users\renu5\Downloads\New folder\Instagram"
$destDir = "C:\Users\renu5\Downloads\New folder\Instagram compressed"

if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir | Out-Null
}

$files = @(Get-ChildItem -Path $sourceDir -File | Where-Object { $_.Name -match "^[n-zN-Z]" })
$originalCount = $files.Count
$originalSize = ($files | Measure-Object -Property Length -Sum).Sum
if ($null -eq $originalSize) { $originalSize = 0 }

if ($originalCount -eq 0) {
    $resultObj = @{
        OriginalCount = 0
        OriginalSizeBytes = 0
        NewSizeBytes = 0
        SpaceSavedBytes = 0
        SuccessCount = 0
        FailCount = 0
    }
    $resultObj | ConvertTo-Json
    exit
}

$scriptBlock = {
    param($fullName, $name, $destDir)
    
    $destFile = Join-Path $destDir $name
    $ext = [System.IO.Path]::GetExtension($name).ToLower()
    
    $success = $false
    $attempts = 0
    
    while (-not $success -and $attempts -lt 3) {
        $attempts++
        
        if ($ext -match "\.(mp4|mov|mkv|avi|webm|m4v|ts)$") {
            & ffmpeg -y -i $fullName -c:v libx264 -crf 28 -preset fast -c:a aac -b:a 128k $destFile 2>&1 | Out-Null
        } elseif ($ext -match "\.(jpg|jpeg|png|webp|bmp|gif)$") {
            & ffmpeg -y -i $fullName -q:v 5 $destFile 2>&1 | Out-Null
        } else {
            return @{ Name = $name; Success = $false; Reason = "Unsupported extension" }
        }
        
        if (Test-Path $destFile) {
            $fi = Get-Item $destFile
            if ($fi.Length -gt 0) {
                $success = $true
            } else {
                Remove-Item $destFile -Force
            }
        }
    }
    
    return @{ Name = $name; Success = $success; DestPath = $destFile }
}

$pool = [runspacefactory]::CreateRunspacePool(1, [Environment]::ProcessorCount)
$pool.Open()

$jobs = @()
foreach ($file in $files) {
    $ps = [powershell]::Create().AddScript($scriptBlock).AddArgument($file.FullName).AddArgument($file.Name).AddArgument($destDir)
    $ps.RunspacePool = $pool
    $jobs += [PSCustomObject]@{
        Runspace = $ps
        IAResult = $ps.BeginInvoke()
    }
}

$successCount = 0
$failCount = 0

foreach ($job in $jobs) {
    $result = $job.Runspace.EndInvoke($job.IAResult)
    $job.Runspace.Dispose()
    
    if ($result.Success) {
        $successCount++
    } else {
        $failCount++
    }
}

$pool.Close()
$pool.Dispose()

$newFiles = @(Get-ChildItem -Path $destDir -File | Where-Object { $_.Name -match "^[n-zN-Z]" })
$newSize = ($newFiles | Measure-Object -Property Length -Sum).Sum
if ($null -eq $newSize) { $newSize = 0 }

$spaceSaved = $originalSize - $newSize

$resultObj = @{
    OriginalCount = $originalCount
    OriginalSizeBytes = $originalSize
    NewSizeBytes = $newSize
    SpaceSavedBytes = $spaceSaved
    SuccessCount = $successCount
    FailCount = $failCount
}

$resultObj | ConvertTo-Json
