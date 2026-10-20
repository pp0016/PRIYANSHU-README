import bpy
import math
import time

def build_motion_scene():
    bpy.ops.wm.read_factory_settings(use_empty=True)
    scene = bpy.context.scene

    # 1. Engine & Output Configuration
    scene.render.engine = 'CYCLES'
    scene.cycles.device = 'CPU'
    scene.cycles.samples = 16
    scene.cycles.use_denoising = True
    scene.cycles.denoiser = 'OPENIMAGEDENOISE'
    scene.cycles.max_bounces = 3
    scene.render.resolution_x = 1920
    scene.render.resolution_y = 1080
    scene.render.resolution_percentage = 100
    scene.render.fps = 30
    scene.frame_start = 1
    scene.frame_end = 60

    # Color Management (AgX if available, else Filmic)
    view_transforms = [item.identifier for item in scene.view_settings.bl_rna.properties['view_transform'].enum_items]
    if 'AgX' in view_transforms:
        scene.view_settings.view_transform = 'AgX'
        scene.view_settings.look = 'Punchy'
    elif 'Filmic' in view_transforms:
        scene.view_settings.view_transform = 'Filmic'
        scene.view_settings.look = 'Medium High Contrast'

    # 2. Materials Setup
    # Gold Metallic Material
    mat_gold = bpy.data.materials.new("ProGoldMetal")
    mat_gold.use_nodes = True
    bsdf_gold = mat_gold.node_tree.nodes.get("Principled BSDF")
    bsdf_gold.inputs["Base Color"].default_value = (1.0, 0.72, 0.18, 1.0)
    bsdf_gold.inputs["Metallic"].default_value = 0.95
    bsdf_gold.inputs["Roughness"].default_value = 0.22

    # Cyan Neon Glow Material
    mat_glow = bpy.data.materials.new("ProCyanGlow")
    mat_glow.use_nodes = True
    bsdf_glow = mat_glow.node_tree.nodes.get("Principled BSDF")
    bsdf_glow.inputs["Base Color"].default_value = (0.0, 0.85, 1.0, 1.0)
    bsdf_glow.inputs["Emission Color"].default_value = (0.0, 0.85, 1.0, 1.0)
    bsdf_glow.inputs["Emission Strength"].default_value = 8.0

    # Dark Obsidian Reflective Floor
    mat_floor = bpy.data.materials.new("ObsidianFloor")
    mat_floor.use_nodes = True
    bsdf_floor = mat_floor.node_tree.nodes.get("Principled BSDF")
    bsdf_floor.inputs["Base Color"].default_value = (0.015, 0.015, 0.02, 1.0)
    bsdf_floor.inputs["Metallic"].default_value = 0.85
    bsdf_floor.inputs["Roughness"].default_value = 0.28

    # 3. Typography Creation (Line 1: Question, Line 2: Hook Highlight)
    # Line 1: "KABHI NOTICE KIYA?"
    curve_l1 = bpy.data.curves.new("TextL1", type='FONT')
    curve_l1.body = "KABHI NOTICE KIYA?"
    curve_l1.size = 0.9
    curve_l1.extrude = 0.12
    curve_l1.bevel_depth = 0.025
    curve_l1.bevel_resolution = 4
    curve_l1.align_x = 'CENTER'
    curve_l1.align_y = 'CENTER'

    obj_l1 = bpy.data.objects.new("ObjTextL1", curve_l1)
    bpy.context.collection.objects.link(obj_l1)
    obj_l1.data.materials.append(mat_gold)
    obj_l1.location = (0, 0, 0.8)

    # Line 2: "TRUST & RESPECT" (Glow Rim + Metallic Face)
    curve_l2 = bpy.data.curves.new("TextL2", type='FONT')
    curve_l2.body = "TRUST & RESPECT"
    curve_l2.size = 1.3
    curve_l2.extrude = 0.16
    curve_l2.bevel_depth = 0.035
    curve_l2.bevel_resolution = 4
    curve_l2.align_x = 'CENTER'
    curve_l2.align_y = 'CENTER'

    obj_l2 = bpy.data.objects.new("ObjTextL2", curve_l2)
    bpy.context.collection.objects.link(obj_l2)
    obj_l2.data.materials.append(mat_glow)
    obj_l2.location = (0, 0, -0.6)

    # Animate Line 1: Eased Scale and Z-entry
    obj_l1.scale = (0.001, 0.001, 0.001)
    obj_l1.keyframe_insert("scale", frame=1)
    obj_l1.scale = (1.08, 1.08, 1.08) # Slight overshoot
    obj_l1.keyframe_insert("scale", frame=18)
    obj_l1.scale = (1.0, 1.0, 1.0)
    obj_l1.keyframe_insert("scale", frame=24)

    # Animate Line 2: Staggered Eased Entry (starts at frame 15)
    obj_l2.scale = (0.001, 0.001, 0.001)
    obj_l2.keyframe_insert("scale", frame=15)
    obj_l2.scale = (1.1, 1.1, 1.1) # Overshoot
    obj_l2.keyframe_insert("scale", frame=32)
    obj_l2.scale = (1.0, 1.0, 1.0)
    obj_l2.keyframe_insert("scale", frame=38)

    # 4. Reflective Backdrop Ground Plane
    plane_data = bpy.data.meshes.new("FloorMesh")
    # Simple quad
    verts = [(-20, -20, -1.8), (20, -20, -1.8), (20, 20, -1.8), (-20, 20, -1.8)]
    faces = [(0, 1, 2, 3)]
    plane_data.from_pydata(verts, [], faces)
    plane_data.update()
    floor_obj = bpy.data.objects.new("FloorObj", plane_data)
    bpy.context.collection.objects.link(floor_obj)
    floor_obj.data.materials.append(mat_floor)

    # 5. Floating Accent Particles (Geometric Diamonds / Tetrahedrons)
    mat_particle = bpy.data.materials.new("ParticleGlow")
    mat_particle.use_nodes = True
    bsdf_part = mat_particle.node_tree.nodes.get("Principled BSDF")
    bsdf_part.inputs["Base Color"].default_value = (0.0, 0.85, 1.0, 1.0)
    bsdf_part.inputs["Emission Color"].default_value = (0.0, 0.85, 1.0, 1.0)
    bsdf_part.inputs["Emission Strength"].default_value = 12.0

    particle_coords = [
        (-4.5, -1.0, 1.8), (-3.2, 0.5, -0.8), (4.2, -0.5, 1.2),
        (3.8, 0.8, -1.0), (-2.0, -1.5, 2.2), (2.5, -1.2, 2.0)
    ]
    for idx, (px, py, pz) in enumerate(particle_coords):
        mesh_p = bpy.data.meshes.new(f"ParticleMesh_{idx}")
        # Small diamond mesh
        d_verts = [(0,0,0.12), (0,0,-0.12), (0.08,0,0), (-0.08,0,0), (0,0.08,0), (0,-0.08,0)]
        d_faces = [(0,2,4), (0,4,3), (0,3,5), (0,5,2), (1,4,2), (1,3,4), (1,5,3), (1,2,5)]
        mesh_p.from_pydata(d_verts, [], d_faces)
        mesh_p.update()
        p_obj = bpy.data.objects.new(f"ParticleObj_{idx}", mesh_p)
        bpy.context.collection.objects.link(p_obj)
        p_obj.data.materials.append(mat_particle)
        p_obj.location = (px, py, pz)
        
        # Subtle drift animation
        p_obj.keyframe_insert("location", frame=1)
        p_obj.location = (px + 0.3 * (1 if idx % 2 == 0 else -1), py, pz + 0.4)
        p_obj.keyframe_insert("location", frame=60)
        p_obj.rotation_euler = (0, 0, 0)
        p_obj.keyframe_insert("rotation_euler", frame=1)
        p_obj.rotation_euler = (0.8, 1.2, 0.5)
        p_obj.keyframe_insert("rotation_euler", frame=60)

    # 6. Four-Point Cinematic Lighting Rig
    # Key Light (Warm soft area)
    key_l = bpy.data.lights.new("KeyLight", type='AREA')
    key_l.energy = 900.0
    key_l.size = 4.0
    key_l.color = (1.0, 0.94, 0.82)
    key_obj = bpy.data.objects.new("KeyObj", key_l)
    key_obj.location = (4.5, -5.5, 4.0)
    key_obj.rotation_euler = (0.9, 0.3, 0.6)
    bpy.context.collection.objects.link(key_obj)

    # Fill Light (Cool ambient soft area)
    fill_l = bpy.data.lights.new("FillLight", type='AREA')
    fill_l.energy = 300.0
    fill_l.size = 6.0
    fill_l.color = (0.7, 0.85, 1.0)
    fill_obj = bpy.data.objects.new("FillObj", fill_l)
    fill_obj.location = (-5.5, -5.0, 2.5)
    fill_obj.rotation_euler = (1.0, -0.3, -0.8)
    bpy.context.collection.objects.link(fill_obj)

    # Rim Kicker (Vibrant Cyan Strip behind subject)
    rim_l = bpy.data.lights.new("RimLight", type='AREA')
    rim_l.energy = 1400.0
    rim_l.size = 6.0
    rim_l.color = (0.0, 0.85, 1.0)
    rim_obj = bpy.data.objects.new("RimObj", rim_l)
    rim_obj.location = (-3.0, 4.0, 2.5)
    rim_obj.rotation_euler = (-1.1, 0.4, 3.0)
    bpy.context.collection.objects.link(rim_obj)

    # Moving Accent Glint / Sweeper Light
    sweep_l = bpy.data.lights.new("SweepLight", type='POINT')
    sweep_l.energy = 600.0
    sweep_l.color = (1.0, 0.9, 0.7)
    sweep_obj = bpy.data.objects.new("SweepObj", sweep_l)
    bpy.context.collection.objects.link(sweep_obj)
    sweep_obj.location = (-6.0, -2.0, 0.8)
    sweep_obj.keyframe_insert("location", frame=20)
    sweep_obj.location = (6.0, -2.0, 0.8)
    sweep_obj.keyframe_insert("location", frame=50)

    # 7. Cinematic Camera Rig with DoF
    cam_target = bpy.data.objects.new("CameraTarget", None)
    cam_target.location = (0, 0, 0.1)
    bpy.context.collection.objects.link(cam_target)

    cam_data = bpy.data.cameras.new("CinemaCamera")
    cam_data.lens = 75.0 # Compression
    cam_data.dof.use_dof = True
    cam_data.dof.focus_object = cam_target
    cam_data.dof.aperture_fstop = 2.2 # Creamy bokeh

    cam_obj = bpy.data.objects.new("CinemaCameraObj", cam_data)
    cam_obj.location = (0.8, -8.5, 1.8)
    bpy.context.collection.objects.link(cam_obj)
    scene.camera = cam_obj

    # Track to target
    track = cam_obj.constraints.new(type='TRACK_TO')
    track.target = cam_target
    track.track_axis = 'TRACK_NEGATIVE_Z'
    track.up_axis = 'UP_Y'

    # Camera Dolly Push-in Animation
    cam_obj.keyframe_insert("location", frame=1)
    cam_obj.location = (0.0, -6.8, 1.1)
    cam_obj.keyframe_insert("location", frame=60)

    print("Complete Motion Graphics scene built successfully!")

build_motion_scene()
