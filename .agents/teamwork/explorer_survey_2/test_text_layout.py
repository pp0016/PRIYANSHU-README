import bpy
import math

# Clean scene
bpy.ops.wm.read_factory_settings(use_empty=True)

# Test creating words procedurally
words = ["HOW", "TO", "WIN", "FRIENDS"]
created_objects = []

total_spacing = 0.3
current_x = 0

for i, word in enumerate(words):
    curve = bpy.data.curves.new(name=f"WordCurve_{word}", type='FONT')
    curve.body = word
    curve.size = 1.0
    curve.extrude = 0.12
    curve.bevel_depth = 0.025
    curve.bevel_resolution = 4
    curve.align_x = 'LEFT'
    curve.align_y = 'CENTER'
    
    obj = bpy.data.objects.new(name=f"WordObj_{word}", object_data=curve)
    bpy.context.collection.objects.link(obj)
    obj.location = (current_x, 0, 0)
    
    # Estimate width (approximate character width for standard font)
    approx_width = len(word) * 0.7 + total_spacing
    current_x += approx_width
    created_objects.append(obj)

print("Created words:", [o.name for o in created_objects])
print("Final current_x:", current_x)
