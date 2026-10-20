import bpy

# Clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)

curve = bpy.data.curves.new(name="TextCurve", type='FONT')
curve.body = "KABHI NOTICE KIYA?"
curve.size = 1.0
curve.extrude = 0.1
curve.bevel_depth = 0.02
curve.bevel_resolution = 3
curve.align_x = 'CENTER'
curve.align_y = 'CENTER'

obj = bpy.data.objects.new(name="TextObj", object_data=curve)
bpy.context.collection.objects.link(obj)

# Evaluate depsgraph
bpy.context.view_layer.update()
depsgraph = bpy.context.evaluated_depsgraph_get()
eval_obj = obj.evaluated_get(depsgraph)

bbox = [list(corner) for corner in eval_obj.bound_box]
xs = [p[0] for p in bbox]
ys = [p[1] for p in bbox]
zs = [p[2] for p in bbox]
width = max(xs) - min(xs)
height = max(ys) - min(ys)
depth = max(zs) - min(zs)

print(f"Evaluated Text Bounding Box: Width={width:.3f}, Height={height:.3f}, Depth={depth:.3f}")
