import bpy

ng = bpy.data.node_groups.new("Test", type="CompositorNodeTree")
glare = ng.nodes.new("CompositorNodeGlare")
print("Glare properties:")
for prop in glare.bl_rna.properties:
    if not prop.identifier.startswith('rna_'):
        print(f"  {prop.identifier}: {prop.type}")
