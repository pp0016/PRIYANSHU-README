import bpy
import os

# --- Configurations ---
IMAGE_PATH = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\.user_uploaded\media_1788285703286.png"

def clear_scene():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()

def setup_camera():
    bpy.ops.object.camera_add(location=(0, -10, 0), rotation=(1.5708, 0, 0))
    cam = bpy.context.active_object
    cam.name = "2D_Camera"
    cam.data.type = 'ORTHO'
    cam.data.ortho_scale = 10
    bpy.context.scene.camera = cam

def setup_reference_image():
    if not os.path.exists(IMAGE_PATH):
        print(f"Image not found at {IMAGE_PATH}")
        return
        
    bpy.ops.object.empty_add(type='IMAGE', location=(0, 0, -0.1), rotation=(1.5708, 0, 0))
    empty = bpy.context.active_object
    empty.name = "Reference_Image"
    
    img = bpy.data.images.load(IMAGE_PATH)
    empty.data.image = img
    empty.empty_display_size = 10

def setup_grease_pencil():
    # Create Grease Pencil object
    bpy.ops.object.gpencil_add(location=(0, 0, 0), type='EMPTY')
    gp_obj = bpy.context.active_object
    gp_obj.name = "Stickman_Character"
    
    # Add Materials
    mat_black = bpy.data.materials.new(name="Black_Stroke")
    bpy.data.materials.create_gpencil_data(mat_black)
    mat_black.grease_pencil.color = (0, 0, 0, 1)
    mat_black.grease_pencil.show_fill = False
    gp_obj.data.materials.append(mat_black)
    
    mat_white = bpy.data.materials.new(name="White_Fill")
    bpy.data.materials.create_gpencil_data(mat_white)
    mat_white.grease_pencil.color = (0, 0, 0, 0)
    mat_white.grease_pencil.show_fill = True
    mat_white.grease_pencil.fill_color = (1, 1, 1, 1)
    gp_obj.data.materials.append(mat_white)

    # Add Layers (Order matters for drawing: bottom to top)
    layers = ['Left_Arm', 'Left_Leg', 'Torso', 'Right_Leg', 'Right_Arm', 'Head', 'Face_Expressions']
    for layer_name in layers:
        gp_obj.data.layers.new(name=layer_name, set_active=True)
        
def setup_timeline():
    # 20 seconds at 24 fps = 480 frames
    bpy.context.scene.render.fps = 24
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 480

def main():
    print("Setting up Stickman 2D Scene...")
    clear_scene()
    setup_camera()
    setup_reference_image()
    setup_timeline()
    setup_grease_pencil()
    print("Scene setup complete!")

if __name__ == "__main__":
    main()
