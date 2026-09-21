# Image Compression Plan

This plan outlines the automated process for compressing the images in `C:\All phones data\mom new one storage` (approx. 2,129 files, 10 GB). 

## Proposed Changes

We will use a PowerShell script (similar to the previous video script) to:
1. Iterate over all image files (`.jpg`, `.jpeg`, `.png`, `.heic`).
2. Compress them using FFmpeg's high-quality JPEG encoder (`ffmpeg -y -i <input> -q:v 3 -update 1 <output>`). My tests show this reduces file sizes by roughly 65% while keeping visual quality virtually identical.
3. Save the compressed files into the same target directory (`C:\All phones data\mom new one storage compressed`), mirroring the exact folder structure.
4. Log the size reductions in `image_compression_log.txt`.

### [NEW] `C:\Users\renu5\Downloads\nishe found\compress_images.ps1`
The PowerShell script that will handle the batch compression in the background.

## User Review Required

> [!CAUTION]  
> After all 2,129 images are successfully compressed and verified, do you want me to automatically **delete the original 10 GB of images** from the main folder just like we did with the videos?

## Verification Plan
- The script will log every single file processed.
- I will run the script as a background task.
- Once it reaches 100%, I will double-check that all 2,129 images were successfully compressed before optionally deleting the originals (based on your answer to the question above).
