import bpy

ng = bpy.data.node_groups.new("Test", type="CompositorNodeTree")
glare = ng.nodes.new("CompositorNodeGlare")
print("Glare inputs:")
for inp in glare.inputs:
    print(f"  {inp.name} (identifier: {inp.identifier}, type: {inp.type})")
print("Glare outputs:")
for out in glare.outputs:
    print(f"  {out.name} (identifier: {out.identifier}, type: {out.type})")
