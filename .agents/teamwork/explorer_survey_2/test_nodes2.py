import bpy

print([t for t in dir(bpy.types) if t.startswith('CompositorNode') and ('comp' in t.lower() or 'out' in t.lower())])
print([t for t in dir(bpy.types) if 'NodeGroup' in t])

# Let's test standard scene compositing in Blender 3.x/4.x/5.x
scene = bpy.context.scene
print("scene attributes:", [a for a in dir(scene) if 'node' in a or 'comp' in a])
