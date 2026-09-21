import bpy
import math
import os
import glob

def build_stickman_mesh():
    parts = []
    head_radius = 0.3
    torso_height = 1.0
    limb_radius = 0.05
    arm_length = 0.8
    leg_length = 0.9
    
    def create_primitive(ptype, location, scale, rotation=(0,0,0)):
        if ptype == 'sphere':
            bpy.ops.mesh.primitive_uv_sphere_add(radius=1, location=location)
        elif ptype == 'cylinder':
            bpy.ops.mesh.primitive_cylinder_add(radius=1, depth=1, location=location)
        obj = bpy.context.active_object
        obj.scale = scale
        obj.rotation_euler = rotation
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        return obj

    torso = create_primitive('cylinder', (0, 0, 1.4), (0.15, 0.15, torso_height/2))
    parts.append(torso)
    
    head = create_primitive('sphere', (0, 0, 1.4 + (torso_height/2) + head_radius), (head_radius, head_radius, head_radius))
    parts.append(head)
    
    arm_l = create_primitive('cylinder', (0.4, 0, 1.7), (limb_radius, limb_radius, arm_length/2), (0, math.radians(90), 0))
    arm_r = create_primitive('cylinder', (-0.4, 0, 1.7), (limb_radius, limb_radius, arm_length/2), (0, math.radians(90), 0))
    parts.extend([arm_l, arm_r])
    
    hand_l = create_primitive('sphere', (0.8, 0, 1.7), (0.08, 0.08, 0.08))
    hand_r = create_primitive('sphere', (-0.8, 0, 1.7), (0.08, 0.08, 0.08))
    parts.extend([hand_l, hand_r])
    
    leg_l = create_primitive('cylinder', (0.15, 0, 0.45), (limb_radius, limb_radius, leg_length/2))
    leg_r = create_primitive('cylinder', (-0.15, 0, 0.45), (limb_radius, limb_radius, leg_length/2))
    parts.extend([leg_l, leg_r])
    
    foot_l = create_primitive('sphere', (0.15, 0, 0), (0.1, 0.1, 0.1))
    foot_r = create_primitive('sphere', (-0.15, 0, 0), (0.1, 0.1, 0.1))
    parts.extend([foot_l, foot_r])
    
    # Context override for joining
    ctx = bpy.context.copy()
    ctx['active_object'] = parts[0]
    ctx['selected_editable_objects'] = parts
    for obj in parts:
        obj.select_set(True)
    bpy.context.view_layer.objects.active = parts[0]
    bpy.ops.object.join()
    
    stickman = parts[0]
    stickman.name = 'Stickman'
    bpy.context.scene.cursor.location = (0, 0, 0)
    bpy.ops.object.origin_set(type='ORIGIN_CURSOR', center='BOUNDS')
    stickman.location = (0, 0, 0)
    return stickman

def apply_toon_shader(obj):
    bpy.context.view_layer.objects.active = obj
    obj.select_set(True)
    
    mat_base = bpy.data.materials.new(name="ToonBase")
    mat_base.use_nodes = True
    nodes = mat_base.node_tree.nodes
    links = mat_base.node_tree.links
    nodes.clear()
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    emission = nodes.new(type='ShaderNodeEmission')
    emission.inputs['Color'].default_value = (1, 1, 1, 1)
    links.new(emission.outputs['Emission'], output.inputs['Surface'])
    
    if obj.data.materials:
        obj.data.materials[0] = mat_base
    else:
        obj.data.materials.append(mat_base)

    mat_outline = bpy.data.materials.new(name="ToonOutline")
    mat_outline.use_nodes = True
    nodes_o = mat_outline.node_tree.nodes
    links_o = mat_outline.node_tree.links
    nodes_o.clear()
    
    output_o = nodes_o.new(type='ShaderNodeOutputMaterial')
    emission_o = nodes_o.new(type='ShaderNodeEmission')
    emission_o.inputs['Color'].default_value = (0, 0, 0, 1)
    links_o.new(emission_o.outputs['Emission'], output_o.inputs['Surface'])
    
    solidify = obj.modifiers.new(name="ToonOutline", type='SOLIDIFY')
    solidify.thickness = 0.05
    solidify.offset = 1
    solidify.use_flip_normals = True
    solidify.material_offset = 1
    
    mat_outline.use_backface_culling = True # Need this for inverted hull
    
    obj.data.materials.append(mat_outline)

def rig_stickman(mesh_obj):
    bpy.ops.object.select_all(action='DESELECT')
    armature = bpy.data.armatures.new("StickmanArmature")
    armature_obj = bpy.data.objects.new("StickmanRig", armature)
    bpy.context.collection.objects.link(armature_obj)
    
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.mode_set(mode='EDIT')
    
    bones = {
        'Root': (0, 0, 0, None),
        'Spine': (0, 0, 1.4, 'Root'),
        'Head': (0, 0, 2.0, 'Spine'),
        'UpperArm.L': (0.4, 0, 1.7, 'Spine'),
        'LowerArm.L': (0.8, 0, 1.7, 'UpperArm.L'),
        'UpperArm.R': (-0.4, 0, 1.7, 'Spine'),
        'LowerArm.R': (-0.8, 0, 1.7, 'UpperArm.R'),
        'Thigh.L': (0.15, 0, 0.9, 'Root'),
        'Shin.L': (0.15, 0, 0.45, 'Thigh.L'),
        'Thigh.R': (-0.15, 0, 0.9, 'Root'),
        'Shin.R': (-0.15, 0, 0.45, 'Thigh.R')
    }
    
    created_bones = {}
    for name, (x, y, z, parent_name) in bones.items():
        bone = armature.edit_bones.new(name)
        bone.head = (x, y, z - 0.2 if name != 'Root' else z)
        bone.tail = (x, y, z)
        created_bones[name] = bone
        
    for name, bone in created_bones.items():
        parent_name = bones[name][3]
        if parent_name:
            bone.parent = created_bones[parent_name]
            bone.use_connect = False
            
    bpy.ops.object.mode_set(mode='OBJECT')
    
    mesh_obj.select_set(True)
    armature_obj.select_set(True)
    bpy.context.view_layer.objects.active = armature_obj
    bpy.ops.object.parent_set(type='ARMATURE_AUTO')
    
    return armature_obj

def animate_stickman(armature):
    bpy.context.view_layer.objects.active = armature
    bpy.ops.object.mode_set(mode='POSE')
    
    # Change bone rotation mode to euler
    for pb in armature.pose.bones:
        pb.rotation_mode = 'XYZ'
    
    b = armature.pose.bones
    bones = {
        'UpperArm.L': b.get('UpperArm.L'),
        'UpperArm.R': b.get('UpperArm.R'),
        'Thigh.L': b.get('Thigh.L'),
        'Thigh.R': b.get('Thigh.R'),
        'Spine': b.get('Spine'),
        'Head': b.get('Head')
    }

    for frame in range(1, 241):
        phase = (frame % 24) / 24 * 2 * math.pi
        
        if bones['UpperArm.L']:
            bones['UpperArm.L'].rotation_euler[0] = math.sin(phase) * 0.5
            bones['UpperArm.L'].keyframe_insert(data_path="rotation_euler", frame=frame)
        if bones['UpperArm.R']:
            bones['UpperArm.R'].rotation_euler[0] = math.sin(phase + math.pi) * 0.5
            bones['UpperArm.R'].keyframe_insert(data_path="rotation_euler", frame=frame)
        if bones['Thigh.L']:
            bones['Thigh.L'].rotation_euler[0] = math.sin(phase + math.pi) * 0.8
            bones['Thigh.L'].keyframe_insert(data_path="rotation_euler", frame=frame)
        if bones['Thigh.R']:
            bones['Thigh.R'].rotation_euler[0] = math.sin(phase) * 0.8
            bones['Thigh.R'].keyframe_insert(data_path="rotation_euler", frame=frame)

    for frame in range(241, 481):
        laugh_intensity = math.sin((frame - 241) * 0.2)
        
        if bones['Spine']:
            bones['Spine'].rotation_euler[0] = laugh_intensity * 0.3
            bones['Spine'].keyframe_insert(data_path="rotation_euler", frame=frame)
        if bones['Head']:
            bones['Head'].rotation_euler[0] = math.sin((frame - 241) * 0.5) * 0.2
            bones['Head'].keyframe_insert(data_path="rotation_euler", frame=frame)

    bpy.ops.object.mode_set(mode='OBJECT')

def render_video():
    # Setup rendering
    bpy.context.scene.render.engine = 'BLENDER_WORKBENCH'
    bpy.context.scene.display.shading.light = 'FLAT'
    bpy.context.scene.display.shading.color_type = 'TEXTURE'
    
    # Add a yellowish background like the image
    bpy.data.worlds["World"].node_tree.nodes["Background"].inputs[0].default_value = (0.9, 0.75, 0.3, 1)

    bpy.context.scene.render.resolution_x = 1080
    bpy.context.scene.render.resolution_y = 1080
    bpy.context.scene.render.fps = 24
    bpy.context.scene.frame_start = 1
    bpy.context.scene.frame_end = 480
    
    cam = bpy.data.cameras.new("OrthoCam")
    cam.type = 'ORTHO'
    cam.ortho_scale = 5.0
    cam_obj = bpy.data.objects.new("OrthoCam", cam)
    bpy.context.collection.objects.link(cam_obj)
    bpy.context.scene.camera = cam_obj
    cam_obj.location = (0, -10, 1.0)
    cam_obj.rotation_euler = (1.5708, 0, 0)
    
    # Output to frames dir
    out_dir = r"C:\Users\renu5\.gemini\antigravity\brain\c1197223-fc12-4a34-a8c8-e5843da5a194\scratch\frames2"
    os.makedirs(out_dir, exist_ok=True)
    bpy.context.scene.render.filepath = os.path.join(out_dir, "frame_")
    bpy.context.scene.render.image_settings.file_format = 'PNG'
    
    print("Starting render...")
    bpy.ops.render.render(animation=True)
    print("Render complete!")

def main():
    bpy.ops.object.select_all(action='SELECT')
    bpy.ops.object.delete()
    
    stickman = build_stickman_mesh()
    apply_toon_shader(stickman)
    rig = rig_stickman(stickman)
    animate_stickman(rig)
    render_video()

if __name__ == "__main__":
    main()
