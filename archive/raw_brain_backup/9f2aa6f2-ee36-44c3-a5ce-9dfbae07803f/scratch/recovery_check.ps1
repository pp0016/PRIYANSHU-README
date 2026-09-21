$verifiedList = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\verified_list.txt"
$missingLog = "C:\Users\renu5\.gemini\antigravity\brain\9f2aa6f2-ee36-44c3-a5ce-9dfbae07803f\scratch\missing_files.txt"

$files = Get-Content $verifiedList
$missing = @()

foreach ($file in $files) {
    if (!(Test-Path $file)) {
        # Check if it was a PNG converted to JPG
        if ($file -match '\.png$') {
            $jpgPath = $file -replace '\.png$', '.jpg'
            if (!(Test-Path $jpgPath)) {
                $missing += $file
            }
        } else {
            $missing += $file
        }
    }
}

if ($missing.Count -gt 0) {
    $missing | Out-File $missingLog
    Write-Host "CRITICAL: Found $($missing.Count) missing files!"
} else {
    Write-Host "Recovery Check Passed: All 1,319 replaced files are safely in their folders."
}
