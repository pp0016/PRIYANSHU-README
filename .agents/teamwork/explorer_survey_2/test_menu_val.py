import bpy

ng = bpy.data.node_groups.new("Test", type="CompositorNodeTree")
glare = ng.nodes.new("CompositorNodeGlare")
type_sock = glare.inputs['Type']
print("Setting to 'Fog Glow'...")
try:
    type_sock.default_value = 'Fog Glow'
    print("Success! Current default_value:", type_sock.default_value)
except Exception as e:
    print("Error:", e)

try:
    type_sock.default_value = 'Bloom'
    print("Success! Bloom default_value:", type_sock.default_value)
except Exception as e:
    print("Error:", e)
