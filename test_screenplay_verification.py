import json
import os
import re

def run_tests():
    print("=== DEEP VERIFICATION SUITE FOR AUTEUR MASTER SCREENPLAY ===")
    
    # 1. Voiceover audio file validation
    audio_path = r'C:\Users\renu5\Downloads\mg-styles-15-test\1st\raw_voiceover_53s.mp3'
    assert os.path.exists(audio_path), f"Audio file not found at {audio_path}"
    audio_size = os.path.getsize(audio_path)
    assert audio_size == 844320, f"Unexpected audio size: {audio_size}"
    print(f"[PASS] Master voiceover file verified: {audio_path} ({audio_size} bytes)")

    # 2. SFX repository validation
    sfx_dir = r'C:\Users\renu5\Downloads\Stick man videos project\ongoing\New folder\stage1_build\sfx'
    assert os.path.exists(sfx_dir), f"SFX directory not found at {sfx_dir}"
    
    # 3. auteur_screenplay.json validation
    json_path = r'C:\Users\renu5\Downloads\mg-styles-15-test\1st\auteur_screenplay.json'
    assert os.path.exists(json_path), f"Screenplay JSON not found at {json_path}"
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    assert "Dale Carnegie" in data.get('project_title')
    assert "How to Win Friends and Influence People" in data.get('project_title')
    assert data.get('fps') == 30
    assert data.get('total_frames') == 1581
    assert data.get('duration_seconds') == 52.70
    assert data.get('zero_frame_gaps') is True
    assert data.get('continuity_verified') is True

    scenes = data.get('scenes', [])
    assert len(scenes) == 12, f"Expected 12 scenes, found {len(scenes)}"
    print(f"[PASS] JSON structure and metadata verified: 12 scenes, 1581 total frames @ 30fps")

    # 4. Strict Frame Continuity & Zero-Gap Validation
    prev_frame_end = -1
    total_duration_frames = 0
    total_whisper_words = 0
    total_sfx_cues = 0

    for i, s in enumerate(scenes):
        s_id = s['scene_id']
        f_start = s['frame_start']
        f_end = s['frame_end']
        dur = s['duration_frames']
        calc_dur = f_end - f_start + 1
        assert dur == calc_dur, f"Scene {s_id} duration mismatch: {dur} vs {calc_dur}"
        assert f_start == prev_frame_end + 1, f"Frame discontinuity at Scene {s_id}: prev end {prev_frame_end}, start {f_start}"
        
        # Word level verification
        w_words = s['spoken_audio']['whisper_words']
        assert len(w_words) > 0, f"Scene {s_id} has no whisper words"
        total_whisper_words += len(w_words)

        for w in w_words:
            assert 'local_frame_start' in w, f"Missing local_frame_start in Scene {s_id}"
            assert 'global_frame_start' in w, f"Missing global_frame_start in Scene {s_id}"
            assert w['local_frame_start'] == max(0, w['global_frame_start'] - f_start), f"Math mismatch in local frame for word {w['word']}"

        # SFX validation
        sfx_items = s['sound_design']
        total_sfx_cues += len(sfx_items)
        for sfx in sfx_items:
            f_path = sfx['sfx_file']
            assert os.path.exists(f_path), f"SFX file does not exist: {f_path}"

        total_duration_frames += dur
        prev_frame_end = f_end

    assert total_duration_frames == 1581, f"Total duration {total_duration_frames} != 1581"
    assert scenes[0]['frame_start'] == 0
    assert scenes[-1]['frame_end'] == 1580
    assert total_whisper_words == 216, f"Expected 216 whisper words, found {total_whisper_words}"
    assert total_sfx_cues == 40, f"Expected 40 SFX cues, found {total_sfx_cues}"
    print(f"[PASS] 100% Contiguous Frame Coverage Verified: 0 dropped frames, 0 dead gaps (0..1580 = 1581 frames)")
    print(f"[PASS] All 216 Whisper words mapped with synchronized global + local sequence frames")
    print(f"[PASS] All 40 local SFX audio cues verified to exist on disk")

    # 5. Master Markdown File Validation
    md_paths = [
        r'C:\Users\renu5\.gemini\antigravity\brain\e0c9c3e2-65fe-4764-83e1-3ae7e149f221\auteur_screenplay_master.md',
        r'C:\Users\renu5\Downloads\mg-styles-15-test\1st\auteur_screenplay_master.md'
    ]
    for md_p in md_paths:
        assert os.path.exists(md_p), f"Markdown missing at {md_p}"
        with open(md_p, 'r', encoding='utf-8') as f:
            md_content = f.read()
        
        # Check all 12 scenes are represented in Markdown
        for s_idx in range(1, 13):
            assert f"### SCENE {s_idx:02d}:" in md_content, f"SCENE {s_idx:02d} header missing in {md_p}"

        # Check Remotion code includes all 12 defined scene components
        for s_idx in range(1, 13):
            # Check scene component definition
            assert f"export const Scene" in md_content, "Missing Scene exports in Remotion code"
        
        assert "Scene01_AnomalyHook: React.FC" in md_content
        assert "Scene02_ParadoxContrast: React.FC" in md_content
        assert "Scene03_InquisitionPivot: React.FC" in md_content
        assert "Scene04_DebunkingMyth: React.FC" in md_content
        assert "Scene05_CanonicalCornerstone: React.FC" in md_content
        assert "Scene06_EthicalInversion: React.FC" in md_content
        assert "Scene07_Tactical01: React.FC" in md_content
        assert "Scene08_Tactical02: React.FC" in md_content
        assert "Scene09_Tactical03: React.FC" in md_content
        assert "Scene10_Tactical04_05: React.FC" in md_content
        assert "Scene11_GoldenTwist: React.FC" in md_content
        assert "Scene12_RetentionAndFourPillars: React.FC" in md_content
        assert "PaperClipSticker: React.FC" in md_content
        assert "KineticWordSpan: React.FC" in md_content
        assert "DaleCarnegieMasterComposition: React.FC" in md_content
        assert "localStartFrame" in md_content

        print(f"[PASS] Markdown synchronized and verified at: {md_p} ({len(md_content)} bytes)")

    print("\n>>> ALL TESTS PASSED SUCCESSFULLY! Master Director Screenplay is 100% verified.")

if __name__ == '__main__':
    run_tests()
