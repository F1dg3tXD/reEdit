import bpy

def align_bones(source_armature, target_armature):
    if source_armature.type != 'ARMATURE' or target_armature.type != 'ARMATURE':
        print("Both selected objects must be armatures.")
        return
    
    bpy.ops.object.mode_set(mode='OBJECT')
    
    source_pose = source_armature.pose
    target_pose = target_armature.pose
    
    bpy.ops.object.mode_set(mode='EDIT')
    
    for bone_name in source_armature.data.bones.keys():
        if bone_name in target_armature.data.bones.keys():
            source_edit_bone = source_armature.data.edit_bones[bone_name]
            target_edit_bone = target_armature.data.edit_bones[bone_name]
            
            source_edit_bone.head = target_edit_bone.head
            source_edit_bone.tail = target_edit_bone.tail
            source_edit_bone.roll = target_edit_bone.roll
    
    bpy.ops.object.mode_set(mode='OBJECT')
    print("Bone alignment complete.")

def main():
    selected_objects = bpy.context.selected_objects
    active_object = bpy.context.view_layer.objects.active
    
    if len(selected_objects) != 2 or active_object not in selected_objects:
        print("Select exactly two armatures, with the reference armature as the active object.")
        return
    
    source_armature = [obj for obj in selected_objects if obj != active_object][0]
    target_armature = active_object
    
    align_bones(source_armature, target_armature)

main()
