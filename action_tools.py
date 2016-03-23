bl_info = {
    "name": "Action Tools",
    "author": "Darknet",
    "version": (2, 7),
    "blender": (2, 65, 4),
    "location": "",
    "description": "Actin Set tools to remove unused sets of animations",
    "warning": "",
    "wiki_url": ""
                "",
    "category": "Tools",
}
#import bmesh
#import os
#import time
import bpy
#import mathutils
#import math
#import random
import operator
#import sys
#from bpy.props import *
#from struct import pack

class Panel_ActionDataPanel( bpy.types.Panel ):

	bl_label        = "Action Set Tool"
	bl_idname       = "OBJECT_PT_ActionDataPanel"
	#bl_space_type  = "PROPERTIES"
	#bl_region_type = "WINDOW"
	#bl_context     = "object"
	bl_space_type   = "VIEW_3D"
	bl_region_type  = "TOOLS"

	#def draw_header(self, context):
	#   layout = self.layout
		#obj = context.object
		#layout.prop(obj, "select", text="")

		#@classmethod
		#def poll(cls, context):
		#   return context.active_object
	def draw(self, context):
		layout = self.layout
		#path = get_dst_path()
		#object_name = ""
		#layout.operator(OBJECT_OT_ActionData.bl_idname)
		layout.operator(OBJECT_OT_ActionData1.bl_idname)
		layout.operator(OBJECT_OT_ActionData2.bl_idname)
		#layout.operator("object.toggle_console")

class OBJECT_OT_ActionData(bpy.types.Operator):
	""" """ \
	""" """
	bl_idname = "object.actiondata"
	bl_label = "Clear All Actions"

	def execute(self, context):
		print("content?")
		for a in bpy.data.actions:
			print(dir(a))
			if a.users == 1 and a.use_fake_user:
				a.user_clear()
		#self.report({'ERROR'}, message)
		return{'FINISHED'}
class OBJECT_OT_ActionData1(bpy.types.Operator):
	""" """ \
	""" """
	bl_idname = "object.actiondata1"
	bl_label = "Clear All Objects Animation Data"

	def execute(self, context):
		print("content?")
		for o in bpy.data.objects:
			o.animation_data_clear()
		for a in bpy.data.actions:
			a.user_clear()
		#self.report({'ERROR'}, message)
		return{'FINISHED'}
class OBJECT_OT_ActionData2(bpy.types.Operator):
	"""Select the mesh for export test. This will create dummy mesh to see which area are broken. """ \
	"""If the vertices share the same position it will cause a bug"""
	bl_idname = "object.actiondata1"
	bl_label = "Select Clear Animation Data"

	def execute(self, context):
		print("content?")
		for o in bpy.data.objects:
			if o.select == True:
				print(o.name)
				o.animation_data_clear()
			#o.animation_data_clear()
		#for a in bpy.data.actions:
			#a.user_clear()
		#self.report({'ERROR'}, message)
		return{'FINISHED'}

#===========================================================================
# Entry
#===========================================================================
def register():
    #print("REGISTER")
    bpy.utils.register_module(__name__)
    #bpy.types.INFO_MT_file_export.append(menu_func)

def unregister():
    #print("UNREGISTER")
    bpy.utils.unregister_module(__name__)
    #bpy.types.INFO_MT_file_export.remove(menu_func)

if __name__ == "__main__":
    #print("\n"*4)
    print(header("Action set tools", 'CENTER'))
    register()
