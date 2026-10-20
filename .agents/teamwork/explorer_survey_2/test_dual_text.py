import bpy

# Clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Technique 1: Layered Outer Glow Bevel + Core Dark Metallic
# Text 1: Core text (slightly smaller bevel, dark metallic)
curve_core = bpy.data.curves.new(name="TextCore", type='FONT')
curve_core.body = "TRUST & RESPECT"
curve_core.size = 1.0
curve_core.extrude = 0.12
curve_core.bevel_depth = 0.01
curve_core.bevel_resolution = 3
curve_core.align_x = 'CENTER'
curve_core.align_y = 'CENTER'

obj_core = bpy.data.objects.new("CoreObj", curve_core)
bpy.context.collection.objects.link(obj_core)

# Text 2: Rim / Glow text (slightly offset in Z or larger bevel, emission material)
curve_rim = bpy.data.curves.new(name="TextRim", type='FONT')
curve_rim.body = "TRUST & RESPECT"
curve_rim.size = 1.0
curve_rim.extrude = 0.10
curve_rim.bevel_depth = 0.035
curve_rim.bevel_resolution = 3
curve_rim.align_x = 'CENTER'
curve_rim.align_y = 'CENTER'

obj_rim = bpy.data.objects.new("RimObj", curve_rim)
bpy.context.collection.objects.link(obj_rim)
obj_rim.location = (0, 0, -0.01) # Sit slightly behind / around

# Materials
mat_metal = bpy.data.materials.new("DarkMetal")
mat_metal.use_nodes = True
bsdf1 = mat_metal.node_tree.nodes.get("Principled BSDF")
bsdf1.inputs["Base Color"].default_value = (0.05, 0.05, 0.08, 1.0)
bsdf1.inputs["Metallic"].default_value = 0.9
bsdf1.inputs["Roughness"].default_value = 0.2

mat_glow = bpy.data.materials.new("NeonCyanGlow")
mat_glow.use_nodes = True
bsdf2 = mat_glow.node_tree.nodes.get("Principled BSDF")
bsdf2.inputs["Base Color"].default_value = (0.0, 0.83, 1.0, 1.0)
bsdf2.inputs["Emission Color"].default_value = (0.0, 0.83, 1.0, 1.0)
bsdf2.inputs["Emission Strength"].default_value = 8.0

obj_core.data.materials.append(mat_metal)
obj_rim.data.materials.append(mat_glow)

print("Dual layered text created successfully!")
