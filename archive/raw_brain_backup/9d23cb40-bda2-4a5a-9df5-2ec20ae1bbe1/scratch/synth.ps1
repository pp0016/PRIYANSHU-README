$dir = 'C:\heygem_data\voice\data'
if (-not (Test-Path -Path $dir)) { New-Item -ItemType Directory -Path $dir -Force }
Add-Type -AssemblyName System.Speech
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SetOutputToWaveFile("$dir\audio.wav")
$text = Get-Content -Path 'C:\Users\renu5\.gemini\antigravity\brain\a1ed586f-c49a-4d2c-9e6d-6fffa2e1a722\scratch\script.txt' -Raw
$synth.Speak($text)
$synth.Dispose()
