import bpy

ng = bpy.data.node_groups.new("Test", type="CompositorNodeTree")
glare = ng.nodes.new("CompositorNodeGlare")
type_sock = glare.inputs['Type']
print("Type socket default_value:", getattr(type_sock, 'default_value', None))
print("Type socket type:", type(type_sock))
print("Type socket attributes:", dir(type_sock))
