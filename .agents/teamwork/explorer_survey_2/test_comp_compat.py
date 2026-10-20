import bpy

scene = bpy.context.scene

def setup_compositor_glare(scene):
    # Support both Blender 3.x/4.x (scene.node_tree) and Blender 5.x+ (scene.compositing_node_group)
    if hasattr(scene, "node_tree") and scene.node_tree is not None:
        tree = scene.node_tree
        tree.nodes.clear()
        rl = tree.nodes.new("CompositorNodeRLayers")
        glare = tree.nodes.new("CompositorNodeGlare")
        glare.glare_type = 'FOG_GLOW'
        glare.quality = 'HIGH'
        glare.threshold = 0.8
        glare.size = 8
        comp = tree.nodes.new("CompositorNodeComposite")
        tree.links.new(rl.outputs['Image'], glare.inputs['Image'])
        tree.links.new(glare.outputs['Image'], comp.inputs['Image'])
        print("Set up legacy/4.x scene.node_tree compositor successfully!")
    elif hasattr(scene, "compositing_node_group"):
        if scene.compositing_node_group is None:
            scene.compositing_node_group = bpy.data.node_groups.new("Compositor", type="CompositorNodeTree")
        tree = scene.compositing_node_group
        tree.nodes.clear()
        rl = tree.nodes.new("CompositorNodeRLayers")
        glare = tree.nodes.new("CompositorNodeGlare")
        glare.glare_type = 'FOG_GLOW'
        glare.quality = 'HIGH'
        glare.threshold = 0.8
        glare.size = 8
        out = tree.nodes.new("NodeGroupOutput")
        # Ensure group output socket exists
        if not tree.interface.items_tree:
            tree.interface.new_socket(name="Image", in_out='OUTPUT', socket_type='NodeSocketColor')
        tree.links.new(rl.outputs['Image'], glare.inputs['Image'])
        tree.links.new(glare.outputs['Image'], out.inputs['Image'])
        print("Set up modern 5.x scene.compositing_node_group compositor successfully!")

setup_compositor_glare(scene)
print("Compositor setup test passed!")
