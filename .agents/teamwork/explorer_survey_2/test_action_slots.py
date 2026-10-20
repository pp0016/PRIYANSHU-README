import bpy

bpy.ops.wm.read_factory_settings(use_empty=True)
obj = bpy.data.objects.new("Test", None)
bpy.context.collection.objects.link(obj)
obj.location = (0, 0, 0)
obj.keyframe_insert(data_path="location", frame=1)
action = obj.animation_data.action

print("Action type:", type(action))
print("Action attributes:", [a for a in dir(action) if not a.startswith('__')])
if hasattr(action, 'layers'):
    print("Action layers:", list(action.layers))
    for layer in action.layers:
        print("  Layer strips:", list(layer.strips))
        for strip in layer.strips:
            print("    Strip channelbags:", list(strip.channelbags))
            for cb in strip.channelbags:
                print("      Channelbag fcurves:", list(cb.fcurves))
if hasattr(action, 'slots'):
    print("Action slots:", list(action.slots))
if hasattr(action, 'curves'):
    print("Action curves:", list(action.curves))
