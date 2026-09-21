# Chat Session: 5ea3e807-6bba-4d1d-a008-04c0fcac2cec

### 🧑 You
<USER_REQUEST>
Find the top 30 largest files in C:\Users\renu5. EXCLUDE the C:\Users\renu5\Downloads directory from your search. Use this command: Get-ChildItem -Path "C:\Users\renu5" -File -Recurse -ErrorAction SilentlyContinue | Where-Object { $_.DirectoryName -notmatch 'C:\\Users\\renu5\\Downloads' } | Sort-Object Length -Descending | Select-Object -First 30 | Select-Object FullName, @{Name="SizeMB";Expression={[math]::Round($_.Length / 1MB, 2)}} | ConvertTo-Json
</USER_REQUEST>
<ADDITIONAL_METADATA>
The current local time is: 2026-08-06T21:37:35+05:30.
</ADDITIONAL_METADATA>

---

