import bpy

scene = bpy.context.scene
print("scene.compositing_node_group:", scene.compositing_node_group)
if scene.compositing_node_group is None:
    ng = bpy.data.node_groups.new("CompositorNodes", type="CompositorNodeTree")
    scene.compositing_node_group = ng
    print("Assigned node group:", scene.compositing_node_group)
    print("Node group type:", type(ng))
    print("Nodes in group:", list(ng.nodes))
    # Add render layers and composite
    rl = ng.nodes.new("CompositorNodeRLayers")
    comp = ng.nodes.new("CompositorNodeComposite")
    glare = ng.nodes.new("CompositorNodeGlare")
    print("Successfully created nodes in compositing_node_group:", [n.name for n in ng.nodes])
