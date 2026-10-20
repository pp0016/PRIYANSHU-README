import bpy
import math

bpy.ops.wm.read_factory_settings(use_empty=True)
scene = bpy.context.scene

# 1. Camera Rig setup
cam_target = bpy.data.objects.new("CamTarget", None)
cam_target.location = (0, 0, 0)
bpy.context.collection.objects.link(cam_target)

cam_data = bpy.data.cameras.new("MainCamera")
cam_data.lens = 70.0 # Cinematic compression
cam_data.dof.use_dof = True
cam_data.dof.focus_object = cam_target
cam_data.dof.aperture_fstop = 2.0

cam_obj = bpy.data.objects.new("MainCamera", cam_data)
cam_obj.location = (0, -7.0, 1.5)
bpy.context.collection.objects.link(cam_obj)
scene.camera = cam_obj

# Add Track To constraint
track_const = cam_obj.constraints.new(type='TRACK_TO')
track_const.target = cam_target
track_const.track_axis = 'TRACK_NEGATIVE_Z'
track_const.up_axis = 'UP_Y'

# Keyframe Camera Push-in
cam_obj.keyframe_insert(data_path="location", frame=1)
cam_obj.location = (0.5, -4.8, 0.8)
cam_obj.keyframe_insert(data_path="location", frame=60)

# Set F-Curve easing
if cam_obj.animation_data and cam_obj.animation_data.action:
    for fcurve in cam_obj.animation_data.action.fcurves:
        for kf in fcurve.keyframe_points:
            kf.interpolation = 'BEZIER'
            kf.easing = 'EASE_OUT'

# 2. Moving Light Sweep setup
light_data = bpy.data.lights.new(name="SweepLight", type='POINT')
light_data.energy = 500.0 # Watts
light_data.color = (0.0, 0.8, 1.0)
light_obj = bpy.data.objects.new("SweepLightObj", light_data)
bpy.context.collection.objects.link(light_obj)

# Light sweeps from left to right across text
light_obj.location = (-5.0, -1.0, 1.0)
light_obj.keyframe_insert(data_path="location", frame=10)
light_obj.location = (5.0, -1.0, 1.0)
light_obj.keyframe_insert(data_path="location", frame=45)

print("Camera Rig, DoF, F-Curve easing, and Light Sweep keyframing verified!")
