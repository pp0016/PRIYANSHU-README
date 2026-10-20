import sys, os, subprocess
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
MGAUDIO_PATH = r"C:\Users\renu5\Downloads\mg-styles-15-test\1st\lib\audio"
sys.path.insert(0, MGAUDIO_PATH)
import mgaudio as mg
from mgaudio import sfx

m = mg.Mix(duration=30.0, bpm=120)

def gunshot(dur=0.7):
    crack = sfx.impact('punch', 1.4)
    pop = sfx.pop('cork', 1.8)
    boom = sfx.boom(dur, 65)
    return mg.layer([(crack, 0, 3, 0), (pop, 0, 2, 0), (boom, 0, 0, 0)])

def book_slam():
    return mg.layer([
        (sfx.paper('flip', dur=0.2), 0, 2, 0),
        (sfx.impact('punch', 1.3), 0.04, 3, 0),
        (sfx.boom(0.8, 48), 0.04, 1, 0)
    ])

def rising_sweep(dur=1.35):
    sw = sfx.riser(dur=dur, kind='sweep')
    sw.sync = 0.0
    return sw

def mechanical_tick():
    return mg.layer([
        (sfx.tick('hi'), 0, 0, 0),
        (sfx.click('wood'), 0.005, -2, 0)
    ])

def page_turn_spread():
    return mg.layer([
        (sfx.paper('flip', dur=0.32), 0, 1.5, 0),
        (sfx.paper('rustle', dur=0.35), 0.04, -2, 0)
    ])

# 15 Clean SFX (Police Siren at 8.16 REMOVED)
# 0.05: Intro paper slate / frame entrance
m.sfx(sfx.paper('slide', dur=0.35), at=0.05)

# 1.08: "Notice kiya?" - curiosity pop
m.sfx(sfx.pop('cork', 1.0), at=1.08)

# 3.12: "Trust aur Respect" - warm chime (C5)
m.sfx(sfx.ding(note=72), at=3.12)

# 6.80: "Aakhir..." - rising tension sweep alert burst
m.sfx(rising_sweep(1.35), at=6.80)

# 8.16: SIREN REMOVED!

# 11.20: "atchi communication skills" - interlocking gear mechanical tick
m.sfx(mechanical_tick(), at=11.20)

# 14.18: "Deeper science" - subtle bell blip (G4)
m.sfx(sfx.blip(note=67), at=14.18)

# 16.04: "Dale Carnegie ki legendary book" - Hero 3D Book Slam impact
m.sfx(book_slam(), at=16.04)

# 19.34: "manipulate karna nahi" - Gunshot crack accent
m.sfx(gunshot(0.7), at=19.34)

# 21.86: "better relationships build" - celebration sparkle chime
m.sfx(sfx.sparkle(dur=0.55), at=21.86)

# 23.36: "Is wonderful book mein" - Tactile page turn & open book spread foley
m.sfx(page_turn_spread(), at=23.36)

# 24.20: "bina argument ke" - Badge 1: '1. NO ARGUMENT' tactile pop hit
m.sfx(sfx.sticker_slap(seed=11), at=24.20)

# 25.00: "apne baat kaise rakhein" - swift low directional gesture whoosh
m.sfx(sfx.whoosh(0.35, 'heavy'), at=25.00)

# 26.20: "criticism..." - Badge 2: '2. NO CRITICISM' punchy tactile slap
m.sfx(sfx.sticker_slap(seed=22), at=26.20)

# 28.20: "dusron ko improve..." - Badge 3: '3. INSPIRE OTHERS' hero shimmer bloom
m.sfx(sfx.shimmer_hit('G5'), at=28.20)

# 28.74: "se inspire karna" - hero star flourish high bell (G5)
m.sfx(sfx.ding(note=79), at=28.74)

SFX_CLEAN_WAV = os.path.join(HERE, 'test_sfx_no_siren.wav')
m.export(SFX_CLEAN_WAV)
print("Clean SFX exported:", SFX_CLEAN_WAV)

TTS_MP3 = r"C:\Users\renu5\Desktop\tts_क्या__20261010_142843.mp3"
OUT_CLEAN_WAV = os.path.join(HERE, 'test_audio_clean_30s.wav')
FFMPEG = r"C:\Users\renu5\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.0.1-full_build\bin\ffmpeg.exe"

subprocess.run([
    FFMPEG, "-y",
    "-t", "30.000000",
    "-i", TTS_MP3,
    "-t", "30.000000",
    "-i", SFX_CLEAN_WAV,
    "-filter_complex", "[0:a]volume=1.0[a0];[1:a]volume=0.9[a1];[a0][a1]amix=inputs=2:duration=first:dropout_transition=0:normalize=0,volume=1.1[outa]",
    "-map", "[outa]",
    "-t", "30.000000",
    "-c:a", "pcm_s16le",
    "-ar", "48000",
    "-ac", "2",
    OUT_CLEAN_WAV
], check=True)
print("Clean 30s mixed audio generated:", OUT_CLEAN_WAV)
