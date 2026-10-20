import bpy

scene = bpy.context.scene
print("Scene attributes with 'comp':", [a for a in dir(scene) if 'comp' in a.lower()])
print("Scene attributes with 'node':", [a for a in dir(scene) if 'node' in a.lower()])

# Check bpy.data.node_groups
print("Node trees in bpy.data:", dir(bpy.data.node_groups))

# Check how to create compositor nodes in Blender 5.x
for attr in dir(scene):
    if 'node' in attr.lower() or 'tree' in attr.lower():
        print(f"Attr: {attr}")

# Let's inspect scene.use_nodes and bpy.context.scene
print("scene.use_nodes:", getattr(scene, 'use_nodes', None))

# Check render engine options
for eng in ['CYCLES', 'BLENDER_EEVEE', 'BLENDER_EEVEE_NEXT', 'BLENDER_WORKBENCH']:
    try:
        scene.render.engine = eng
        print(f"Engine {eng} accepted successfully!")
    except Exception as e:
        print(f"Engine {eng} error: {e}")
