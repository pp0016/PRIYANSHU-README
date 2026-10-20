import bpy
import time

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# Configure Cycles CPU
scene.render.engine = 'CYCLES'
scene.cycles.device = 'CPU'
scene.cycles.samples = 16
scene.cycles.use_denoising = True
scene.cycles.denoiser = 'OPENIMAGEDENOISE'
scene.cycles.max_bounces = 3
scene.cycles.diffuse_bounces = 1
scene.cycles.glossy_bounces = 2
scene.cycles.transmission_bounces = 2
scene.cycles.volume_bounces = 0
scene.cycles.transparent_max_bounces = 4

# Resolution
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Color Management (AgX if available, else Filmic)
if 'AgX' in [item.identifier for item in scene.view_settings.bl_rna.properties['view_transform'].enum_items]:
    scene.view_settings.view_transform = 'AgX'
    scene.view_settings.look = 'Punchy'
else:
    scene.view_settings.view_transform = 'Filmic'
    scene.view_settings.look = 'Medium High Contrast'

# Create Text
curve = bpy.data.curves.new("HookText", type='FONT')
curve.body = "KABHI NOTICE KIYA?"
curve.size = 1.0
curve.extrude = 0.15
curve.bevel_depth = 0.03
curve.bevel_resolution = 4
curve.align_x = 'CENTER'
curve.align_y = 'CENTER'

obj = bpy.data.objects.new("HookTextObj", curve)
bpy.context.collection.objects.link(obj)

# Material: Brushed Gold / Cyan Metallic with Emission Rim
mat = bpy.data.materials.new("GoldMetal")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (1.0, 0.75, 0.2, 1.0) # Gold
bsdf.inputs["Metallic"].default_value = 0.95
bsdf.inputs["Roughness"].default_value = 0.25
obj.data.materials.append(mat)

# Emissive Accent Plane / Floor
plane_mesh = bpy.data.meshes.new("FloorMesh")
plane_obj = bpy.data.objects.new("FloorObj", plane_mesh)
bpy.context.collection.objects.link(plane_obj)
plane_obj.location = (0, 0, -1.0)
plane_obj.scale = (15, 15, 1)

mat_floor = bpy.data.materials.new("DarkFloor")
mat_floor.use_nodes = True
bsdf_floor = mat_floor.node_tree.nodes.get("Principled BSDF")
bsdf_floor.inputs["Base Color"].default_value = (0.01, 0.01, 0.02, 1.0)
bsdf_floor.inputs["Roughness"].default_value = 0.3
bsdf_floor.inputs["Metallic"].default_value = 0.8
plane_obj.data.materials.append(mat_floor)

# Lighting: Three-point studio lighting + neon rim
key_light = bpy.data.lights.new("KeyLight", type='AREA')
key_light.energy = 800.0
key_light.size = 3.0
key_light.color = (1.0, 0.95, 0.85)
key_obj = bpy.data.objects.new("KeyLightObj", key_light)
key_obj.location = (4.0, -5.0, 4.0)
bpy.context.collection.objects.link(key_obj)

rim_light = bpy.data.lights.new("RimLight", type='AREA')
rim_light.energy = 1200.0
rim_light.size = 4.0
rim_light.color = (0.0, 0.8, 1.0) # Cyan rim
rim_obj = bpy.data.objects.new("RimLightObj", rim_light)
rim_obj.location = (-4.0, 5.0, 2.0)
bpy.context.collection.objects.link(rim_obj)

# Camera
cam_data = bpy.data.cameras.new("Cam")
cam_data.lens = 65.0
cam_obj = bpy.data.objects.new("CamObj", cam_data)
cam_obj.location = (0, -6.5, 1.2)
cam_obj.rotation_euler = (1.42, 0, 0)
bpy.context.collection.objects.link(cam_obj)
scene.camera = cam_obj

# Output
scene.render.filepath = "c:/Users/renu5/Downloads/priyanshu readme/.agents/teamwork/explorer_survey_2/render_test_frame.png"
scene.render.image_settings.file_format = 'PNG'

print("Starting render...")
t0 = time.time()
bpy.ops.render.render(write_still=True)
t1 = time.time()
print(f"Render completed in {t1 - t0:.2f} seconds!")
