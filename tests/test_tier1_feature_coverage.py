"""Tier 1: Feature Coverage Test Suite.

Tests cover:
- CLI argument parsing (defaults, overrides, frame bounds, text inputs, sample counts)
- Headless execution with zero GUI dependencies
- Procedural 3D text geometry (curves, bevel, extrude, resolution, alignment)
- Advanced procedural materials & shaders (Gold Metallic, Neon Cyan Emission, Obsidian Floor, Particle Luminescence)
- 4-point studio lighting rig (Key, Fill, Rim, Sweep glint)
- Cinematic 75mm camera rig with Track-To constraint and DoF bokeh
- Cycles CPU engine cloud optimization settings (OIDN, adaptive sampling, clamped bounces)
"""

import os
import sys
import json
import unittest
import subprocess
from pathlib import Path

# Add tests directory to sys.path
TESTS_DIR = Path(__file__).resolve().parent
if str(TESTS_DIR) not in sys.path:
    sys.path.insert(0, str(TESTS_DIR))

from test_helpers import (
    TARGET_REPO_ROOT,
    WORKSPACE_ROOT,
    find_blender_binary,
    run_blender_script,
)


class TestTier1FeatureCoverage(unittest.TestCase):
    """Tier 1 test suite verifying functional feature completeness."""

    @classmethod
    def setUpClass(cls):
        cls.scene_script = TARGET_REPO_ROOT / "blender" / "scene_generator.py"
        cls.blender_bin = find_blender_binary()
        if not cls.scene_script.exists():
            raise FileNotFoundError(f"Target script not found: {cls.scene_script}")

    def test_cli_parsing_defaults_and_overrides(self):
        """Verify CLI parser behavior for defaults and custom flags."""
        introspect_code = f"""
import sys
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator
import json

# Test 1: Defaults
cfg_default = scene_generator.parse_args(["blender", "-b", "-P", "scene_generator.py"])

# Test 2: Blender native flags
cfg_native = scene_generator.parse_args([
    "blender", "-b", "-P", "scene_generator.py",
    "-s", "10", "-e", "45", "-o", "//custom/frame_#####",
    "--samples", "48", "--text1", "HOOK TITLE", "--text2", "IMPACT"
])

# Test 3: Trailing argument separator '--'
cfg_trailing = scene_generator.parse_args([
    "blender", "-b", "-P", "scene_generator.py", "--",
    "--start", "5", "--end", "25", "--samples", "16",
    "--text1", "CUSTOM 1", "--text2", "CUSTOM 2"
])

result = {{
    "default": cfg_default,
    "native": cfg_native,
    "trailing": cfg_trailing
}}
print("CLI_RESULT_JSON:" + json.dumps(result))
"""
        cmd = [
            self.blender_bin, "-b", "--python-expr", introspect_code
        ] if self.blender_bin else [sys.executable, "-c", introspect_code]

        res = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        self.assertEqual(res.returncode, 0, f"CLI parsing failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("CLI_RESULT_JSON:"):
                data = json.loads(line.replace("CLI_RESULT_JSON:", ""))
                # Validate defaults
                self.assertEqual(data["default"]["start"], 1)
                self.assertIn(data["default"]["end"], (60, 120))
                self.assertEqual(data["default"]["text1"], "KABHI NOTICE KIYA?")
                self.assertEqual(data["default"]["text2"], "TRUST & RESPECT")

                # Validate native flags
                self.assertEqual(data["native"]["start"], 10)
                self.assertEqual(data["native"]["end"], 45)
                self.assertEqual(data["native"]["output"], "//custom/frame_#####")
                self.assertEqual(data["native"]["samples"], 48)
                self.assertEqual(data["native"]["text1"], "HOOK TITLE")
                self.assertEqual(data["native"]["text2"], "IMPACT")

                # Validate trailing args
                self.assertEqual(data["trailing"]["start"], 5)
                self.assertEqual(data["trailing"]["end"], 25)
                self.assertEqual(data["trailing"]["samples"], 16)
                self.assertEqual(data["trailing"]["text1"], "CUSTOM 1")
                self.assertEqual(data["trailing"]["text2"], "CUSTOM 2")
                break
        else:
            self.fail("Did not find CLI_RESULT_JSON in stdout")

    def test_headless_execution_zero_gui(self):
        """Verify the script executes completely headlessly without GUI dependencies."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        res = subprocess.run(
            [self.blender_bin, "-b", "-P", str(self.scene_script)],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Headless execution failed: {res.stderr}")
        self.assertIn("Procedural 3D Scene successfully built", res.stdout)

    def test_procedural_typography_geometry(self):
        """Verify 3D text curves have required extrusion, bevel, resolution, and hierarchy."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        introspect_code = f"""
import sys, json, bpy
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator

scene = scene_generator.build_scene()

obj_l1 = bpy.data.objects.get("ObjTextL1")
obj_l2 = bpy.data.objects.get("ObjTextL2")

curve_l1 = obj_l1.data if obj_l1 else None
curve_l2 = obj_l2.data if obj_l2 else None

data = {{
    "l1_exists": obj_l1 is not None,
    "l2_exists": obj_l2 is not None,
    "l1_body": curve_l1.body if curve_l1 else "",
    "l2_body": curve_l2.body if curve_l2 else "",
    "l1_size": curve_l1.size if curve_l1 else 0.0,
    "l2_size": curve_l2.size if curve_l2 else 0.0,
    "l1_extrude": curve_l1.extrude if curve_l1 else 0.0,
    "l2_extrude": curve_l2.extrude if curve_l2 else 0.0,
    "l1_bevel_depth": curve_l1.bevel_depth if curve_l1 else 0.0,
    "l2_bevel_depth": curve_l2.bevel_depth if curve_l2 else 0.0,
    "l1_bevel_res": curve_l1.bevel_resolution if curve_l1 else 0,
    "l2_bevel_res": curve_l2.bevel_resolution if curve_l2 else 0,
    "l1_align_x": curve_l1.align_x if curve_l1 else "",
    "l2_align_x": curve_l2.align_x if curve_l2 else "",
}}
print("TYPOGRAPHY_GEOMETRY_JSON:" + json.dumps(data))
"""
        res = subprocess.run(
            [self.blender_bin, "-b", "--python-expr", introspect_code],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Introspection failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("TYPOGRAPHY_GEOMETRY_JSON:"):
                d = json.loads(line.replace("TYPOGRAPHY_GEOMETRY_JSON:", ""))
                self.assertTrue(d["l1_exists"], "ObjTextL1 does not exist")
                self.assertTrue(d["l2_exists"], "ObjTextL2 does not exist")
                self.assertEqual(d["l1_body"], "KABHI NOTICE KIYA?")
                self.assertEqual(d["l2_body"], "TRUST & RESPECT")

                # Geometric Bevel & Extrude Specifications from baseline_spec.md
                self.assertGreaterEqual(d["l1_extrude"], 0.10, "L1 extrude below spec")
                self.assertGreaterEqual(d["l2_extrude"], 0.14, "L2 extrude below spec")
                self.assertGreaterEqual(d["l1_bevel_depth"], 0.020, "L1 bevel depth below spec")
                self.assertGreaterEqual(d["l2_bevel_depth"], 0.030, "L2 bevel depth below spec")
                self.assertGreaterEqual(d["l1_bevel_res"], 4, "L1 bevel resolution below spec")
                self.assertGreaterEqual(d["l2_bevel_res"], 4, "L2 bevel resolution below spec")
                self.assertEqual(d["l1_align_x"], "CENTER")
                self.assertEqual(d["l2_align_x"], "CENTER")

                # Visual Hierarchy Check (L2 impact keyword should be larger than L1 question)
                self.assertGreater(d["l2_size"], d["l1_size"], "L2 font size must exceed L1")
                break
        else:
            self.fail("TYPOGRAPHY_GEOMETRY_JSON not found in output")

    def test_advanced_pbr_materials_and_floor(self):
        """Verify Principled BSDF procedural materials (Gold, Cyan Glow, Obsidian Floor, Particles)."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        introspect_code = f"""
import sys, json, bpy
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator

scene = scene_generator.build_scene()

def get_bsdf_val(mat_name, socket_name):
    mat = bpy.data.materials.get(mat_name)
    if not mat or not mat.use_nodes:
        return None
    bsdf = mat.node_tree.nodes.get("Principled BSDF")
    if not bsdf or socket_name not in bsdf.inputs:
        return None
    val = bsdf.inputs[socket_name].default_value
    if hasattr(val, '__iter__'):
        return list(val)
    return val

gold_met = get_bsdf_val("ProGoldMetal", "Metallic")
gold_rough = get_bsdf_val("ProGoldMetal", "Roughness")
glow_str = get_bsdf_val("ProCyanGlow", "Emission Strength")
floor_met = get_bsdf_val("ObsidianFloor", "Metallic")
floor_rough = get_bsdf_val("ObsidianFloor", "Roughness")
part_str = get_bsdf_val("ParticleGlow", "Emission Strength")

floor_obj = bpy.data.objects.get("FloorObj")

data = {{
    "has_gold": bpy.data.materials.get("ProGoldMetal") is not None,
    "gold_metallic": gold_met,
    "gold_roughness": gold_rough,
    "has_glow": bpy.data.materials.get("ProCyanGlow") is not None,
    "glow_strength": glow_str,
    "has_floor": bpy.data.materials.get("ObsidianFloor") is not None,
    "floor_metallic": floor_met,
    "floor_roughness": floor_rough,
    "floor_obj_exists": floor_obj is not None,
    "part_strength": part_str
}}
print("MATERIALS_JSON:" + json.dumps(data))
"""
        res = subprocess.run(
            [self.blender_bin, "-b", "--python-expr", introspect_code],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Material inspection failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("MATERIALS_JSON:"):
                d = json.loads(line.replace("MATERIALS_JSON:", ""))
                self.assertTrue(d["has_gold"], "ProGoldMetal material missing")
                self.assertGreaterEqual(d["gold_metallic"], 0.90, "Gold metallic under 0.90")
                self.assertLessEqual(d["gold_roughness"], 0.30, "Gold roughness exceeds 0.30")

                self.assertTrue(d["has_glow"], "ProCyanGlow material missing")
                self.assertGreaterEqual(d["glow_strength"], 5.0, "Cyan glow emission under 5.0")

                self.assertTrue(d["has_floor"], "ObsidianFloor material missing")
                self.assertGreaterEqual(d["floor_metallic"], 0.70, "Floor metallic under 0.70")
                self.assertTrue(d["floor_obj_exists"], "FloorObj missing from scene")

                self.assertGreaterEqual(d["part_strength"], 8.0, "Particle emission under 8.0")
                break
        else:
            self.fail("MATERIALS_JSON not found in output")

    def test_four_point_studio_lighting_rig(self):
        """Verify 4-point lighting rig (Key, Fill, Rim, Sweep) configuration and animation."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        introspect_code = f"""
import sys, json, bpy
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator

scene = scene_generator.build_scene()

key = bpy.data.lights.get("KeyLight")
fill = bpy.data.lights.get("FillLight")
rim = bpy.data.lights.get("RimLight")
sweep = bpy.data.lights.get("SweepLight")
sweep_obj = bpy.data.objects.get("SweepObj")

has_sweep_anim = False
if sweep_obj and sweep_obj.animation_data and sweep_obj.animation_data.action:
    has_sweep_anim = len(sweep_obj.animation_data.action.fcurves) > 0

data = {{
    "key_exists": key is not None,
    "key_type": key.type if key else "",
    "key_energy": key.energy if key else 0,
    "fill_exists": fill is not None,
    "fill_type": fill.type if fill else "",
    "fill_energy": fill.energy if fill else 0,
    "rim_exists": rim is not None,
    "rim_type": rim.type if rim else "",
    "rim_energy": rim.energy if rim else 0,
    "sweep_exists": sweep is not None,
    "sweep_type": sweep.type if sweep else "",
    "sweep_energy": sweep.energy if sweep else 0,
    "sweep_animated": has_sweep_anim
}}
print("LIGHTING_JSON:" + json.dumps(data))
"""
        res = subprocess.run(
            [self.blender_bin, "-b", "--python-expr", introspect_code],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Lighting inspection failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("LIGHTING_JSON:"):
                d = json.loads(line.replace("LIGHTING_JSON:", ""))
                self.assertTrue(d["key_exists"], "KeyLight missing")
                self.assertEqual(d["key_type"], "AREA")
                self.assertGreaterEqual(d["key_energy"], 800.0)

                self.assertTrue(d["fill_exists"], "FillLight missing")
                self.assertEqual(d["fill_type"], "AREA")
                self.assertGreaterEqual(d["fill_energy"], 200.0)

                self.assertTrue(d["rim_exists"], "RimLight missing")
                self.assertEqual(d["rim_type"], "AREA")
                self.assertGreaterEqual(d["rim_energy"], 1000.0)

                self.assertTrue(d["sweep_exists"], "SweepLight missing")
                self.assertGreaterEqual(d["sweep_energy"], 400.0)
                self.assertTrue(d["sweep_animated"], "Sweep glint light must be keyframe animated")
                break
        else:
            self.fail("LIGHTING_JSON not found in output")

    def test_cinematic_camera_rig_and_dof(self):
        """Verify 75mm lens, DoF f/2.2 bokeh, Track-To constraint, and dolly push-in."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        introspect_code = f"""
import sys, json, bpy
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator

scene = scene_generator.build_scene()

cam_obj = bpy.data.objects.get("CinemaCameraObj")
cam_data = cam_obj.data if cam_obj else None

track_constraint = None
if cam_obj:
    for c in cam_obj.constraints:
        if c.type == 'TRACK_TO':
            track_constraint = c
            break

has_dolly = False
if cam_obj and cam_obj.animation_data and cam_obj.animation_data.action:
    has_dolly = any(fc.data_path == "location" for fc in cam_obj.animation_data.action.fcurves)

data = {{
    "cam_exists": cam_obj is not None,
    "lens": cam_data.lens if cam_data else 0.0,
    "use_dof": cam_data.dof.use_dof if cam_data else False,
    "fstop": cam_data.dof.aperture_fstop if cam_data else 0.0,
    "has_track_to": track_constraint is not None,
    "has_dolly_animation": has_dolly
}}
print("CAMERA_JSON:" + json.dumps(data))
"""
        res = subprocess.run(
            [self.blender_bin, "-b", "--python-expr", introspect_code],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Camera inspection failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("CAMERA_JSON:"):
                d = json.loads(line.replace("CAMERA_JSON:", ""))
                self.assertTrue(d["cam_exists"], "CinemaCameraObj missing")
                self.assertEqual(d["lens"], 75.0, "Camera focal length must be 75mm for telephoto compression")
                self.assertTrue(d["use_dof"], "Depth of Field must be enabled")
                self.assertLessEqual(d["fstop"], 2.8, "Aperture f-stop must be <= 2.8 for bokeh")
                self.assertTrue(d["has_track_to"], "Camera must have Track-To constraint")
                self.assertTrue(d["has_dolly_animation"], "Camera must have keyframed dolly push-in animation")
                break
        else:
            self.fail("CAMERA_JSON not found in output")

    def test_cycles_cpu_cloud_engine_configuration(self):
        """Verify Cycles CPU engine, OIDN denoiser, adaptive sampling, and bounce clamping."""
        if not self.blender_bin:
            self.skipTest("Blender executable not available on this runner")

        introspect_code = f"""
import sys, json, bpy
sys.path.insert(0, r"{self.scene_script.parent}")
import scene_generator

scene = scene_generator.build_scene()

data = {{
    "engine": scene.render.engine,
    "device": scene.cycles.device,
    "denoising": scene.cycles.use_denoising,
    "denoiser": scene.cycles.denoiser,
    "adaptive_sampling": scene.cycles.use_adaptive_sampling,
    "adaptive_threshold": scene.cycles.adaptive_threshold,
    "max_bounces": scene.cycles.max_bounces,
    "volume_bounces": scene.cycles.volume_bounces,
    "res_x": scene.render.resolution_x,
    "res_y": scene.render.resolution_y,
    "fps": scene.render.fps,
    "persistent_data": scene.render.use_persistent_data
}}
print("CYCLES_CONFIG_JSON:" + json.dumps(data))
"""
        res = subprocess.run(
            [self.blender_bin, "-b", "--python-expr", introspect_code],
            capture_output=True,
            text=True,
            timeout=45
        )
        self.assertEqual(res.returncode, 0, f"Cycles config inspection failed: {res.stderr}")

        for line in res.stdout.splitlines():
            if line.startswith("CYCLES_CONFIG_JSON:"):
                d = json.loads(line.replace("CYCLES_CONFIG_JSON:", ""))
                self.assertEqual(d["engine"], "CYCLES")
                self.assertEqual(d["device"], "CPU")
                self.assertTrue(d["denoising"], "Cycles denoising must be enabled")
                self.assertEqual(d["denoiser"], "OPENIMAGEDENOISE")
                self.assertTrue(d["adaptive_sampling"], "Adaptive sampling must be enabled")
                self.assertLessEqual(d["adaptive_threshold"], 0.05)
                self.assertLessEqual(d["max_bounces"], 4)
                self.assertEqual(d["volume_bounces"], 0)
                self.assertEqual(d["res_x"], 1920)
                self.assertEqual(d["res_y"], 1080)
                self.assertEqual(d["fps"], 30)
                self.assertTrue(d["persistent_data"], "use_persistent_data must be enabled for CI speedup")
                break
        else:
            self.fail("CYCLES_CONFIG_JSON not found in output")


if __name__ == "__main__":
    unittest.main()
