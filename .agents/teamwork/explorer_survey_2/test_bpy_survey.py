import bpy

print("=== BLENDER SYSTEM INFO ===")
print("Blender version:", bpy.app.version_string)

scene = bpy.context.scene
render = scene.render

print("\n=== AVAILABLE RENDER ENGINES ===")
engine_prop = scene.render.bl_rna.properties['engine']
for item in engine_prop.enum_items:
    print(f"Engine: {item.identifier} ({item.name})")

print("\n=== COLOR MANAGEMENT VIEW TRANSFORMS ===")
view_prop = scene.view_settings.bl_rna.properties['view_transform']
for item in view_prop.enum_items:
    print(f"View Transform: {item.identifier} ({item.name})")

print("\n=== EEVEE PROPERTIES IN THIS VERSION ===")
if hasattr(scene, 'eevee'):
    eevee_props = dir(scene.eevee)
    print("Has 'use_bloom'?", hasattr(scene.eevee, 'use_bloom'))
    print("Eevee attributes sample:", [p for p in eevee_props if not p.startswith('_')][:20])

print("\n=== PRINCIPLED BSDF INPUT SOCKETS ===")
mat = bpy.data.materials.new(name="TestMat")
mat.use_nodes = True
bsdf = mat.node_tree.nodes.get("Principled BSDF")
if bsdf:
    print("Principled BSDF inputs:")
    for inp in bsdf.inputs:
        print(f"  - {inp.name} (type: {inp.type})")
bpy.data.materials.remove(mat)

print("\n=== COMPOSITOR NODE TYPES ===")
scene.use_nodes = True
tree = scene.node_tree
print("Compositing node tree available. Glare node check:")
try:
    glare = tree.nodes.new(type="CompositorNodeGlare")
    print("Glare node created successfully:", glare.name)
    print("Glare gl_type enum items:")
    for item in glare.bl_rna.properties['glare_type'].enum_items:
        print(f"  - {item.identifier} ({item.name})")
    tree.nodes.remove(glare)
except Exception as e:
    print("Error creating glare node:", e)

print("\n=== CURVE FONT TEXT OBJECT CREATION ===")
font_curve = bpy.data.curves.new(name="TestFont", type='FONT')
font_curve.body = "HOW TO WIN FRIENDS"
font_curve.extrude = 0.1
font_curve.bevel_depth = 0.02
font_curve.bevel_resolution = 4
font_curve.align_x = 'CENTER'
font_curve.align_y = 'CENTER'
font_obj = bpy.data.objects.new("TestTextObj", font_curve)
bpy.context.collection.objects.link(font_obj)
print(f"Created font object: {font_obj.name}, body='{font_curve.body}', extrude={font_curve.extrude}, bevel={font_curve.bevel_depth}")

print("\n=== TEST COMPLETED SUCCESSFULLY ===")
