$sourceDir = "C:\mom phone storage"
$compressedDir = "C:\mom phone storage compressed"
$verifiedListPath = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\verified_list.txt"
$failedListPath = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\failed_files.txt"

if (!(Test-Path $verifiedListPath)) {
    Write-Host "Verified list not found!"
    exit
}

$verifiedFiles = Get-Content $verifiedListPath

$movedCount = 0
foreach ($originalPath in $verifiedFiles) {
    if (Test-Path $originalPath) {
        $relativePath = $originalPath.Substring($sourceDir.Length + 1)
        $compressedPath = Join-Path $compressedDir $relativePath

        # Adjust for PNG -> JPG renaming
        if ($compressedPath -match '\.png$') {
            if (!(Test-Path $compressedPath)) {
                $compressedPath = $compressedPath -replace '\.png$', '.jpg'
            }
        }

        if (Test-Path $compressedPath) {
            # Delete the large original file
            Remove-Item -Path $originalPath -Force
            
            # Determine target path (if extension changed, use new extension)
            $targetPath = Join-Path (Split-Path $originalPath -Parent) (Split-Path $compressedPath -Leaf)
            
            # Move compressed file to original location
            Move-Item -Path $compressedPath -Destination $targetPath -Force
            $movedCount++
        }
    }
}

Write-Host "Successfully deleted and replaced $movedCount files."

# Identify the 8 failed files by cross-referencing delete_list.md with verified_list.txt
$deleteListPath = "$compressedDir\delete_list.md"
$allLines = Get-Content $deleteListPath | Where-Object { $_ -match '^- ' } | ForEach-Object { $_.Substring(2) } | Select-Object -Unique

$failedFiles = @()
foreach ($file in $allLines) {
    if ($verifiedFiles -notcontains $file) {
        $failedFiles += $file
    }
}

$failedFiles | Out-File -FilePath $failedListPath -Encoding utf8
Write-Host "Logged $($failedFiles.Count) failed files."
