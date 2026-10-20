import bpy
import time

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# Configure EEVEE
scene.render.engine = 'BLENDER_EEVEE'
scene.eevee.taa_render_samples = 16

# Resolution
scene.render.resolution_x = 1920
scene.render.resolution_y = 1080
scene.render.resolution_percentage = 100

# Text & Camera
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

mat = bpy.data.materials.new("GoldMetal")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")
bsdf.inputs["Base Color"].default_value = (1.0, 0.75, 0.2, 1.0)
bsdf.inputs["Metallic"].default_value = 0.95
bsdf.inputs["Roughness"].default_value = 0.25
obj.data.materials.append(mat)

key_light = bpy.data.lights.new("KeyLight", type='AREA')
key_light.energy = 800.0
key_obj = bpy.data.objects.new("KeyLightObj", key_light)
key_obj.location = (4.0, -5.0, 4.0)
bpy.context.collection.objects.link(key_obj)

cam_data = bpy.data.cameras.new("Cam")
cam_obj = bpy.data.objects.new("CamObj", cam_data)
cam_obj.location = (0, -6.5, 1.2)
cam_obj.rotation_euler = (1.42, 0, 0)
bpy.context.collection.objects.link(cam_obj)
scene.camera = cam_obj

scene.render.filepath = "c:/Users/renu5/Downloads/priyanshu readme/.agents/teamwork/explorer_survey_2/render_eevee_test.png"
scene.render.image_settings.file_format = 'PNG'

print("Starting EEVEE render...")
t0 = time.time()
bpy.ops.render.render(write_still=True)
t1 = time.time()
print(f"EEVEE Render completed in {t1 - t0:.2f} seconds!")
