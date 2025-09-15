# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

import bpy
import bpy.utils.previews
import os
from bpy_extras.io_utils import ImportHelper, ExportHelper
from .Main import device as SoundDevice

addon_keymaps = {}
_icons = None


def display_collection_id(uid, vars):
    id = f"coll_{uid}"
    for var in vars.keys():
        if var.startswith("i_"):
            id += f"_{var}_{vars[var]}"
    return id


class SNA_UL_display_collection_list_C4F01(bpy.types.UIList):

    def draw_item(self, context, layout, data, item_C4F01, icon, active_data, active_propname, index_C4F01):
        row = layout
        row_6A288 = layout.row(heading='', align=False)
        row_6A288.alert = False
        row_6A288.enabled = True
        row_6A288.active = True
        row_6A288.use_property_split = False
        row_6A288.use_property_decorate = False
        row_6A288.scale_x = 1.0
        row_6A288.scale_y = 1.0
        row_6A288.alignment = 'Expand'.upper()
        row_6A288.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_6A288.label(text=item_C4F01['Name'], icon_value=0)
        row_6A288.label(text=item_C4F01['Collection'], icon_value=0)

    def filter_items(self, context, data, propname):
        flt_flags = []
        for item in getattr(data, propname):
            if not self.filter_name or self.filter_name.lower() in item.name.lower():
                if True:
                    flt_flags.append(self.bitflag_filter_item)
                else:
                    flt_flags.append(0)
            else:
                flt_flags.append(0)
        return flt_flags, []


def property_exists(prop_path, glob, loc):
    try:
        eval(prop_path, glob, loc)
        return True
    except:
        return False


def ShowMessageBoxer(title, icon, message):
    scene = bpy.context.scene
    # Access the 2D cursor location
    cursor_location = scene.cursor.location 

    def draw(self, context):
        self.layout.label(text=message)
    bpy.context.window_manager.popup_menu(draw, title=title, icon=icon)


class SNA_PT_PLAY_SOUNDS_D9E41(bpy.types.Panel):
    bl_label = 'Play Sounds'
    bl_idname = 'SNA_PT_PLAY_SOUNDS_D9E41'
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_context = ''
    bl_category = 'Play Sounds'
    bl_order = 0
    bl_ui_units_x=0

    @classmethod
    def poll(cls, context):
        return not (False)

    def draw_header(self, context):
        layout = self.layout

    def draw(self, context):
        layout = self.layout
        row_EC17D = layout.row(heading='', align=False)
        row_EC17D.alert = False
        row_EC17D.enabled = True
        row_EC17D.active = True
        row_EC17D.use_property_split = False
        row_EC17D.use_property_decorate = False
        row_EC17D.scale_x = 1.0
        row_EC17D.scale_y = 1.0
        row_EC17D.alignment = 'Expand'.upper()
        row_EC17D.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_EC17D.label(text='Collection Name:', icon_value=0)
        row_EC17D.label(text='Sound Collection:', icon_value=0)
        coll_id = display_collection_id('C4F01', locals())
        layout.template_list('SNA_UL_display_collection_list_C4F01', coll_id, bpy.context.preferences.addons[__package__].preferences, 'sna_sounds', bpy.context.preferences.addons[__package__].preferences, 'sna_index_sounds', rows=0)
        layout.prop(bpy.context.scene, 'sna_sound_name', text='Name', icon_value=0, emboss=True)
        row_A8CC6 = layout.row(heading='', align=True)
        row_A8CC6.alert = False
        row_A8CC6.enabled = True
        row_A8CC6.active = True
        row_A8CC6.use_property_split = False
        row_A8CC6.use_property_decorate = False
        row_A8CC6.scale_x = 1.0
        row_A8CC6.scale_y = 1.0
        row_A8CC6.alignment = 'Expand'.upper()
        row_A8CC6.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_A8CC6.prop(bpy.context.scene, 'sna_sounds_path', text='Path', icon_value=0, emboss=True)
        row_7CAE5 = row_A8CC6.row(heading='', align=True)
        row_7CAE5.alert = False
        row_7CAE5.enabled = True
        row_7CAE5.active = True
        row_7CAE5.use_property_split = False
        row_7CAE5.use_property_decorate = False
        row_7CAE5.scale_x = 1.2100000381469727
        row_7CAE5.scale_y = 1.0
        row_7CAE5.alignment = 'Expand'.upper()
        row_7CAE5.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_7CAE5.operator('sna.ps_findsoundcollectionpath_4efbb', text='', icon_value=133, emboss=True, depress=False)
        layout.prop(bpy.context.scene, 'sna_collection_to_find', text='Collection', icon_value=0, emboss=True)
        row_034FF = layout.row(heading='', align=True)
        row_034FF.alert = False
        row_034FF.enabled = True
        row_034FF.active = True
        row_034FF.use_property_split = False
        row_034FF.use_property_decorate = False
        row_034FF.scale_x = 1.0
        row_034FF.scale_y = 1.0
        row_034FF.alignment = 'Expand'.upper()
        row_034FF.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        row_50A6B = row_034FF.row(heading='', align=True)
        row_50A6B.alert = False
        row_50A6B.enabled = True
        row_50A6B.active = True
        row_50A6B.use_property_split = False
        row_50A6B.use_property_decorate = False
        row_50A6B.scale_x = 3.0
        row_50A6B.scale_y = 1.0
        row_50A6B.alignment = 'Expand'.upper()
        row_50A6B.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_50A6B.operator('sna.ps_addtosounds_92268', text='Add', icon_value=0, emboss=True, depress=False)
        op.sna_sc_name = bpy.context.scene.sna_sound_name
        op.sna_sc_path = bpy.context.scene.sna_sounds_path
        op.sna_bc_look = bpy.context.scene.sna_collection_to_find
        op.sna_bc_where = ''
        row_07784 = row_034FF.row(heading='', align=True)
        row_07784.alert = False
        row_07784.enabled = (property_exists("bpy.context.preferences.addons[__package__].preferences.sna_sounds", globals(), locals()) and len(bpy.context.preferences.addons[__package__].preferences.sna_sounds) > 0)
        row_07784.active = True
        row_07784.use_property_split = False
        row_07784.use_property_decorate = False
        row_07784.scale_x = 1.0
        row_07784.scale_y = 1.0
        row_07784.alignment = 'Expand'.upper()
        row_07784.operator_context = "INVOKE_DEFAULT" if True else "EXEC_DEFAULT"
        op = row_07784.operator('sna.ps_removefromsounds_bb050', text='', icon_value=91, emboss=True, depress=False)
        op = layout.operator('sna.ps_stopallsounds_4e55aa', text='Stop All Sounds', emboss=True, depress=False)


class SNA_AddonPreferences_E700A(bpy.types.AddonPreferences):
    bl_idname = __package__
    sna_sounds: bpy.props.CollectionProperty(name='Sounds', description='', type=bpy.types.PropertyGroup.__subclasses__()[0])
    sna_index_sounds: bpy.props.IntProperty(name='Index Sounds', description='', default=0, subtype='NONE')

    def draw(self, context):
        if not (False):
            layout = self.layout 

class SNA_OT_Ps_StopAllSounds_4e55aa(bpy.types.Operator):
    bl_idname = "sna.ps_stopallsounds_4e55aa"
    bl_label = "ps_StopAllSounds"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    def execute(self, context):
        SoundDevice.stopAll()
        return {"FINISHED"}


class SNA_OT_Ps_Findsoundcollectionpath_4Efbb(bpy.types.Operator, ExportHelper):
    bl_idname = "sna.ps_findsoundcollectionpath_4efbb"
    bl_label = "ps_FindSoundCollectionPath"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    filter_glob: bpy.props.StringProperty( default=' ', options={'HIDDEN'} )
    filename_ext = ' '

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        bpy.context.scene.sna_sounds_path = self.filepath.replace('\\', '/')
        return {"FINISHED"}


class SNA_OT_Ps_Addtosounds_92268(bpy.types.Operator):
    bl_idname = "sna.ps_addtosounds_92268"
    bl_label = "ps_AddToSounds"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}
    sna_sc_name: bpy.props.StringProperty(name='SC_Name', description='', default='', subtype='NONE', maxlen=0)
    sna_sc_path: bpy.props.StringProperty(name='SC_Path', description='', default='', subtype='NONE', maxlen=0)
    sna_bc_look: bpy.props.StringProperty(name='BC_look', description='', default='', subtype='NONE', maxlen=0)
    sna_bc_where: bpy.props.StringProperty(name='BC_Where', description='', default='', subtype='NONE', maxlen=0)

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if ((self.sna_sc_name == '') or (self.sna_sc_path == '') or (self.sna_bc_look == '')):
            ShowMessageBoxer('! ERROR !',
                                                              'WARNING_LARGE',
                                                              'Inputs Empty')
        else:
            item_1DA8D = bpy.context.preferences.addons[__package__].preferences.sna_sounds.add()
            item_1DA8D['Name'] = self.sna_sc_name
            item_1DA8D['Path'] = self.sna_sc_path
            item_1DA8D['Collection'] = self.sna_bc_look
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


class SNA_OT_Ps_Removefromsounds_Bb050(bpy.types.Operator):
    bl_idname = "sna.ps_removefromsounds_bb050"
    bl_label = "ps_RemoveFromSounds"
    bl_description = ""
    bl_options = {"REGISTER", "UNDO"}

    @classmethod
    def poll(cls, context):
        if bpy.app.version >= (3, 0, 0) and True:
            cls.poll_message_set('')
        return not False

    def execute(self, context):
        if (property_exists("bpy.context.preferences.addons[__package__].preferences.sna_sounds", globals(), locals()) and len(bpy.context.preferences.addons[__package__].preferences.sna_sounds) > bpy.context.preferences.addons[__package__].preferences.sna_index_sounds):
            if len(bpy.context.preferences.addons[__package__].preferences.sna_sounds) > bpy.context.preferences.addons[__package__].preferences.sna_index_sounds:
                bpy.context.preferences.addons[__package__].preferences.sna_sounds.remove(bpy.context.preferences.addons[__package__].preferences.sna_index_sounds)
        else:
            ShowMessageBoxer('! ERROR !',
                                                              'WARNING_LARGE',
                                                              'No Data')
        return {"FINISHED"}

    def invoke(self, context, event):
        return self.execute(context)


def register():
    global _icons
    _icons = bpy.utils.previews.new()
    bpy.types.Scene.sna_sound_name = bpy.props.StringProperty(name='Sound Name', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_sounds_path = bpy.props.StringProperty(name='Sounds Path', description='', default='', subtype='NONE', maxlen=0)
    bpy.types.Scene.sna_collection_to_find = bpy.props.StringProperty(name='Collection To Find', description='', default='', subtype='NONE', maxlen=0)


def unregister():
    global _icons
    bpy.utils.previews.remove(_icons)
    wm = bpy.context.window_manager
    kc = wm.keyconfigs.addon
    for km, kmi in addon_keymaps.values():
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()
    del bpy.types.Scene.sna_collection_to_find
    del bpy.types.Scene.sna_sounds_path
    del bpy.types.Scene.sna_sound_name
