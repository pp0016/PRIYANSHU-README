# Windows Forensic Storage Cleanup Guide

As requested, here is your expert-level guide to deep-cleaning your laptop. I've broken this down from standard safe methods to advanced CMD techniques that IT professionals use.

> [!CAUTION]
> Before running advanced commands or deleting large system files, ensure you don't have any ongoing Windows Updates. It's also always good practice to have a backup of important personal files.

## 1. The "Advanced" CMD & PowerShell Tools

You mentioned seeing people use CMD to clean their laptops. Here are the most effective and safe commands you can run as an Administrator to reclaim space.

### The Component Store Cleanup (DISM)
The `WinSxS` folder stores older versions of Windows components and updates. It grows massively over time. You can safely clean superseded updates using the Deployment Image Servicing and Management (DISM) tool.

1. Open your Start Menu, type `cmd`, right-click **Command Prompt**, and select **Run as administrator**.
2. Run this command to see if a cleanup is recommended:
   ```cmd
   dism.exe /Online /Cleanup-Image /AnalyzeComponentStore
   ```
3. If it says cleanup is recommended, run this command to actually clean it (this will take some time):
   ```cmd
   dism.exe /Online /Cleanup-Image /StartComponentCleanup
   ```
   *(Note: Adding `/ResetBase` to the end of that command reclaims even more space, but you will not be able to uninstall current Windows updates afterward.)*

### DNS Cache Flush
This won't save gigabytes of space, but it's a standard IT practice for cleaning temporary network data and resolving internet issues.
```cmd
ipconfig /flushdns
```

## 2. Built-in Windows Storage Tools (The Safest Route)

Windows has powerful built-in tools that often do a better job than third-party "cleaners".

### Disk Cleanup (System Files)
1. Press `Win + R`, type `cleanmgr`, and press Enter.
2. Select your `C:` drive.
3. Click the **Clean up system files** button (requires admin rights).
4. Select `C:` again.
5. Check almost everything in the list, paying special attention to:
   - **Windows Update Cleanup** (Can be several GBs)
   - **Previous Windows installation(s)** (Can be 10-20 GBs if you recently upgraded)
   - **Temporary Files**
6. Click OK.

### Storage Sense
1. Open **Settings** > **System** > **Storage**.
2. Turn on **Storage Sense**.
3. Click **Configure Storage Sense or run it now**.
4. Set it to run automatically, and at the bottom, click **Clean now** for an immediate sweep.

## 3. Manual Cache Clearing

### The Temp Folders
Windows and applications store temporary files in specific folders. It is completely safe to delete the *contents* of these folders (though some files currently in use might refuse to delete—just skip those).

1. Press `Win + R`, type `%temp%`, and press Enter. (This opens `C:\Users\YourUser\AppData\Local\Temp`). Delete everything inside.
2. Press `Win + R`, type `temp`, and press Enter. (This opens `C:\Windows\Temp`). Delete everything inside.
3. Press `Win + R`, type `prefetch`, and press Enter. Delete everything inside. (Windows uses these to load apps faster, but cleaning them occasionally is fine).

### Browser Caches
Browsers are notorious for hogging storage. In Chrome/Edge/Firefox:
1. Press `Ctrl + Shift + Delete`.
2. Select **All time** or **Everything**.
3. Check **Cached images and files** (leave passwords and cookies unchecked if you want to stay logged in).
4. Click Clear.

## 4. How to Find the Hidden "Storage Hogs"

Since my automated scanners hit some permission roadblocks on your system, here is the exact, safe PowerShell command you can run yourself to find the top 30 largest files on your `C:\` drive.

1. Open PowerShell as Administrator.
2. Paste this command and hit Enter:

```powershell
Get-ChildItem -Path C:\ -File -Recurse -ErrorAction SilentlyContinue | Sort-Object Length -Descending | Select-Object -First 30 | Select-Object Directory, Name, @{Name="Size(MB)";Expression={[math]::Round($_.Length / 1MB, 2)}} | Out-GridView
```
*This will open a nice pop-up window (`Out-GridView`) showing you the exact locations of the largest files, making it easy for you to review them manually.*
