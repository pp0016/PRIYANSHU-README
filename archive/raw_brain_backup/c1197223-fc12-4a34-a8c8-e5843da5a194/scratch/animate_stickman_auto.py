import bpy
import math
import os

# Paths
bored_img_path = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch\stickman_bored.png"
laugh_img_path = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch\stickman_laugh.png"
output_video_path = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch\stickman_animation.mp4"

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_camera():
    bpy.ops.object.camera_add(location=(0, -5, 0), rotation=(math.radians(90), 0, 0))
    cam = bpy.context.active_object
    cam.name = "Camera"
    bpy.context.scene.camera = cam
    # Use orthographic to avoid perspective distortion
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = 5.5

def create_material(name, img_path):
    mat = bpy.data.materials.new(name=name)
    mat.use_nodes = True
    nodes = mat.node_tree.nodes
    links = mat.node_tree.links
    
    # Clear default nodes
    for n in nodes:
        nodes.remove(n)
        
    # Create nodes
    bsdf = nodes.new(type='ShaderNodeBsdfPrincipled')
    bsdf.location = (0, 0)
    
    tex_image = nodes.new('ShaderNodeTexImage')
    tex_image.image = bpy.data.images.load(img_path)
    tex_image.location = (-300, 0)
    
    output = nodes.new('ShaderNodeOutputMaterial')
    output.location = (300, 0)
    
    # Link nodes
    links.new(tex_image.outputs['Color'], bsdf.inputs['Base Color'])
    links.new(tex_image.outputs['Alpha'], bsdf.inputs['Alpha'])
    links.new(bsdf.outputs['BSDF'], output.inputs['Surface'])
    
    # Removed blend_method and shadow_method as they are deprecated in EEVEE Next
    
    return mat

def setup_scene():
    bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
    bpy.context.scene.display.shading.light = 'FLAT'
    bpy.context.scene.display.shading.color_type = 'TEXTURE'
    
    # Set background color to yellow/tan matching the original drawing
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.9, 0.75, 0.3, 1)
    
    # Add Empty as parent
    bpy.ops.object.empty_add(type='PLAIN_AXES', location=(0, 0, 0))
    empty = bpy.context.active_object
    empty.name = "Stickman_Rig"
    
    mat_bored = create_material("Mat_Bored", bored_img_path)
    mat_laugh = create_material("Mat_Laugh", laugh_img_path)
    
    def create_plane(name, mat):
        bpy.ops.mesh.primitive_plane_add(size=1, enter_editmode=False, align='WORLD', location=(0, 0, 0))
        plane = bpy.context.active_object
        plane.name = name
        plane.rotation_euler[0] = math.radians(90)
        plane.scale[0] = 3.62
        plane.scale[1] = 4.65
        plane.scale[2] = 1
        bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
        plane.data.materials.append(mat)
        plane.parent = empty
        return plane

    plane_bored = create_plane("Bored", mat_bored)
    plane_laugh = create_plane("Laugh", mat_laugh)
    
    # Hide Laugh plane initially
    plane_laugh.hide_render = True
    plane_laugh.hide_viewport = True
    
    # Add a light
    bpy.ops.object.light_add(type='SUN', location=(0, -5, 5))
    
    return empty, plane_bored, plane_laugh

def animate_stickman(empty, plane_bored, plane_laugh):
    fps = 24
    bpy.context.scene.render.fps = fps
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 480  # 20 seconds
    
    # 0-240 (Walk cycle)
    walk_cycle_frames = 24
    for f in range(1, 241, walk_cycle_frames):
        empty.location = (0, 0, -0.2)
        empty.rotation_euler[1] = 0
        empty.keyframe_insert(data_path="location", frame=f)
        empty.keyframe_insert(data_path="rotation_euler", frame=f)
        
        empty.location = (0, 0, 0)
        empty.rotation_euler[1] = math.radians(5)
        empty.keyframe_insert(data_path="location", frame=f + 6)
        empty.keyframe_insert(data_path="rotation_euler", frame=f + 6)
        
        empty.location = (0, 0, -0.2)
        empty.rotation_euler[1] = 0
        empty.keyframe_insert(data_path="location", frame=f + 12)
        empty.keyframe_insert(data_path="rotation_euler", frame=f + 12)
        
        empty.location = (0, 0, 0)
        empty.rotation_euler[1] = math.radians(-5)
        empty.keyframe_insert(data_path="location", frame=f + 18)
        empty.keyframe_insert(data_path="rotation_euler", frame=f + 18)
        
    # Swap visibility at frame 240
    plane_bored.hide_render = False
    plane_bored.hide_viewport = False
    plane_bored.keyframe_insert(data_path="hide_render", frame=239)
    plane_bored.keyframe_insert(data_path="hide_viewport", frame=239)
    
    plane_bored.hide_render = True
    plane_bored.hide_viewport = True
    plane_bored.keyframe_insert(data_path="hide_render", frame=240)
    plane_bored.keyframe_insert(data_path="hide_viewport", frame=240)

    plane_laugh.hide_render = True
    plane_laugh.hide_viewport = True
    plane_laugh.keyframe_insert(data_path="hide_render", frame=239)
    plane_laugh.keyframe_insert(data_path="hide_viewport", frame=239)
    
    plane_laugh.hide_render = False
    plane_laugh.hide_viewport = False
    plane_laugh.keyframe_insert(data_path="hide_render", frame=240)
    plane_laugh.keyframe_insert(data_path="hide_viewport", frame=240)
    
    # 240-480 (Laugh cycle)
    laugh_cycle_frames = 12
    for f in range(240, 481, laugh_cycle_frames):
        empty.location = (0, 0, -0.1)
        empty.rotation_euler[0] = 0
        empty.keyframe_insert(data_path="location", frame=f)
        empty.keyframe_insert(data_path="rotation_euler", frame=f)
        
        empty.location = (0, 0, 0.2)
        empty.rotation_euler[0] = math.radians(10) # tilt head back slightly
        empty.keyframe_insert(data_path="location", frame=f + 6)
        empty.keyframe_insert(data_path="rotation_euler", frame=f + 6)

def render_video():
    import glob
    
    # Render PNG sequence to a temp directory
    render_dir = os.path.join(os.path.dirname(output_video_path), "frames")
    os.makedirs(render_dir, exist_ok=True)
    bpy.context.scene.render.filepath = os.path.join(render_dir, "frame_")
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    
    print("Starting render...")
    bpy.ops.render.render(animation=True)
    print("Render complete!")

def main():
    clear_scene()
    setup_camera()
    empty, plane_bored, plane_laugh = setup_scene()
    animate_stickman(empty, plane_bored, plane_laugh)
    render_video()

if __name__ == "__main__":
    main()
