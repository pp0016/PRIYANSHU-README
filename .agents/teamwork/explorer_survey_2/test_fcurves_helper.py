import bpy

def get_action_fcurves(obj):
    if not obj.animation_data or not obj.animation_data.action:
        return []
    act = obj.animation_data.action
    if hasattr(act, 'fcurves'):
        return list(act.fcurves)
    fcurves = []
    if hasattr(act, 'layers'):
        for layer in act.layers:
            for strip in layer.strips:
                for cb in strip.channelbags:
                    fcurves.extend(cb.fcurves)
    return fcurves

bpy.ops.wm.read_factory_settings(use_empty=True)
obj = bpy.data.objects.new("Test", None)
bpy.context.collection.objects.link(obj)
obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=1)
obj.location = (10, 0, 0)
obj.keyframe_insert(data_path="location", frame=30)

curves = get_action_fcurves(obj)
print(f"Extracted {len(curves)} F-Curves successfully!")
for fc in curves:
    print(f"FCurve data_path={fc.data_path}, index={fc.array_index}, points={len(fc.keyframe_points)}")
    for kp in fc.keyframe_points:
        kp.interpolation = 'BEZIER'
        kp.easing = 'EASE_OUT'

print("Set interpolation and easing on all keyframes successfully!")
