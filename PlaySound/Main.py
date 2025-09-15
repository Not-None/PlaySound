import bpy
import aud
import os
import random

last_sel_object = None
last_sel_bone = None
device = aud.Device()

def play_sound(path):
    sound = aud.Sound(path)
    device.play(sound)

def compare_col_names():

    obj_collection = {collection.name for collection in bpy.context.active_object.users_collection}

    matching_inds = []
    try:
        for idx, item in enumerate(bpy.context.preferences.addons[__package__].preferences.sna_sounds):
            if item["Collection"] in obj_collection:
                matching_inds.append((item["Collection"], idx))
    except AttributeError:
        print("Error: 'soundcollection' is not a valid collection or lacks 'Collection' attribute")
        return []
    
    # # Output results
    # if matching_inds:
    #     print("Matching names and indices in other_set:")
    #     for name, idx in matching_inds:
    #         print(f"Name: {name}, Index: {idx}")
    # else:
    #     print("No matching names found")

    return matching_inds

def sel_change(dgraph):
    global last_sel_object
    global last_sel_bone
    if bpy.context.active_object != last_sel_object or bpy.context.active_pose_bone != last_sel_bone:
        last_sel_object = bpy.context.active_object
        if bpy.context.mode == "POSE":
            last_sel_bone = bpy.context.active_pose_bone
        
        # play_sound("C:/Sounds/PIGMAN RAP  ZAMination Version (Minecraft Animation Music Video)Dan Bull - ZAMination.mp3")
        soundcollection = bpy.context.preferences.addons[__package__].preferences.sna_sounds
        
        common = compare_col_names()

        for item, idx in common:
            
            SoundList = os.listdir(soundcollection[idx]["Path"])
            SCLen = len(SoundList)

            RPlay = random.randrange(0, SCLen)

            path = soundcollection[idx]["Path"] + SoundList[RPlay]
            play_sound(path)
            
            

# class PT_ps_Panel(bpy.types.Panel):
    

bpy.app.handlers.depsgraph_update_post.clear()
bpy.app.handlers.depsgraph_update_post.append(sel_change)