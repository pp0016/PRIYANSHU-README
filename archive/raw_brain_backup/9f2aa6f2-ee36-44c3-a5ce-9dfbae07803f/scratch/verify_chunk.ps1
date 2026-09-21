param(
    [int]$StartOffset = 0,
    [int]$Count = 0,
    [string]$OutputFile = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\verified_list.txt"
)

$sourceDir = "C:\mom phone storage"
$destDir = "C:\mom phone storage compressed"
$deleteListPath = "$destDir\delete_list.md"

if (!(Test-Path $deleteListPath)) {
    Write-Host "No delete list found."
    exit
}

# Read all lines that start with "- C:\mom phone storage"
$lines = Get-Content $deleteListPath | Where-Object { $_ -match '^- ' } | ForEach-Object { $_.Substring(2) }

# Deduplicate in case any file was written twice
$lines = $lines | Select-Object -Unique

$totalLines = @($lines).Count
if ($Count -eq 0 -or $StartOffset + $Count -gt $totalLines) {
    $Count = $totalLines - $StartOffset
}

if ($Count -le 0) {
    Write-Host "No lines to process for offset $StartOffset."
    exit
}

$subset = $lines | Select-Object -Skip $StartOffset -First $Count
Write-Host "Verifying $($subset.Count) files..."

$validFiles = @()
$failedFiles = @()

foreach ($originalPath in $subset) {
    if (!(Test-Path $originalPath)) {
        # Already deleted or missing
        continue
    }

    $relativePath = $originalPath.Substring($sourceDir.Length + 1)
    $destPath = Join-Path $destDir $relativePath
    
    # Handle PNG to JPG renaming
    if ($destPath -match '\.png$') {
        if (!(Test-Path $destPath)) {
            $destPath = $destPath -replace '\.png$', '.jpg'
        }
    }

    if (Test-Path $destPath) {
        $originalSize = (Get-Item $originalPath).Length
        $compressedSize = (Get-Item $destPath).Length

        if ($compressedSize -lt $originalSize -and $compressedSize -gt 0) {
            $validFiles += $originalPath
        } else {
            $failedFiles += $originalPath
        }
    } else {
        $failedFiles += $originalPath
    }
}

$validFiles | Out-File -FilePath $OutputFile -Encoding utf8
Write-Host "Verification complete. Valid files: $($validFiles.Count), Failed: $($failedFiles.Count)"
