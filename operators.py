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
import sys,inspect
from bpy.types import Operator



##########_____ DISPLAY TYPE RELATED _____##########

class Set_Display_As_Wire(Operator):
	"""Set 'Wire' display method for the selected object"""
	bl_label="Set Wire Display Type"
	bl_idname="object.set_display_as_wire"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):	
		for obj in context.selected_objects:					
			obj.display_type = 'WIRE'
		return{'FINISHED'}

class Set_Display_As_Solid(Operator):
	"""Set 'Solid' display method for the selected object"""
	bl_label="Set Solid Display Type"
	bl_idname="object.set_display_as_solid"
	bl_options={'REGISTER','UNDO'}
	
	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):	
		for obj in context.selected_objects:			
			obj.display_type = 'SOLID'
		return{'FINISHED'}

class Set_Display_As_Textured(Operator):
	"""Set 'Textured' display method for the selected object"""
	bl_label="Set Textured Display Type"
	bl_idname="object.set_display_as_textured"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):	
		for obj in context.selected_objects:						
			obj.display_type = 'TEXTURED'
		return{'FINISHED'}




##########_____ BOUNDS RELATED _____##########

def check_and_set_bounds(context,obj):
	if context.scene.fast_toggle.operation_upon=='bounds':
		obj.display_type = 'BOUNDS'
		obj.show_bounds=False
	elif obj.display_type=='BOUNDS':
		obj.display_type='SOLID'

class Set_Bounds_Display_Box(Operator):
	"""Set bounds display as 'BOX'"""
	bl_label="Set Bounds Display -> Box"
	bl_idname="object.set_bounds_display_box"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:				
			obj.show_bounds = True
			check_and_set_bounds(context,obj)
			obj.display_bounds_type = 'BOX'

		return{'FINISHED'}

class Set_Bounds_Display_Sphere(Operator):
	"""Set bounds display as 'Sphere'"""
	bl_label="Set Bounds Display -> Sphere"
	bl_idname="object.set_bounds_display_sphere"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = True
			check_and_set_bounds(context,obj)
			obj.display_bounds_type = 'SPHERE'

		return{'FINISHED'}

class Set_Bounds_Display_Cone(Operator):
	"""Set bounds display as 'Cone'"""
	bl_label="Set Bounds Display -> Cone"
	bl_idname="object.set_bounds_display_cone"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = True
			check_and_set_bounds(context,obj)
			obj.display_bounds_type = 'CONE'

		return{'FINISHED'}

class Set_Bounds_Display_Cylinder(Operator):
	"""Set bounds display as 'Cylinder'"""
	bl_label="Set Bounds Display -> Cylinder"
	bl_idname="object.set_bounds_display_cylinder"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = True
			check_and_set_bounds(context,obj)
			obj.display_bounds_type = 'CYLINDER'

		return{'FINISHED'}

class Set_Bounds_Display_Capsule(Operator):
	"""Set bounds display as 'Capsule'"""
	bl_label="Set Bounds Display -> Capsule"
	bl_idname="object.set_bounds_display_capsule"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = True
			check_and_set_bounds(context,obj)
			obj.display_bounds_type = 'CAPSULE'

		return{'FINISHED'}

class Disable_Bounds_Display(Operator):
	"""Disable bounds display"""
	bl_label="Disable Bounds Display"
	bl_idname="object.disable_bounds_display"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
	
	def execute(self,context):
		for obj in context.selected_objects:
			if obj.display_type=='BOUNDS':
				obj.display_type='SOLID'
			obj.show_bounds = False
		# context.scene.fast_toggle.operation_upon='object'
		return{'FINISHED'}

class Enable_Wireframe(Operator):
	"""Enable Wireframe Display"""
	bl_label="Enable Wireframe Display"
	bl_idname="object.enable_wireframe"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_wire = True
		return{'FINISHED'}

class Disable_Wireframe(Operator):
	"""Disable Wireframe Display"""
	bl_label="Disable Wireframe Display"
	bl_idname="object.disable_wireframe"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_wire = False
		return{'FINISHED'}

class Enable_Axis(Operator):
	"""Enable Axis"""
	bl_label="Enable Axis"
	bl_idname="object.enable_axis"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_axis = True
		return{'FINISHED'}

class Disable_Axis(Operator):
	"""Disable Axis"""
	bl_label="Disable Axis"
	bl_idname="object.disable_axis"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_axis = False
		return{'FINISHED'}

class Show_Name(Operator):
	"""SHow Name"""
	bl_label="Show Name"
	bl_idname="object.show_name"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_name = True
		return{'FINISHED'}

class Hide_Name(Operator):
	"""Hide Name"""
	bl_label="Hide Name"
	bl_idname="object.hide_name"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_name = False
		return{'FINISHED'}

class Enable_In_Front(Operator):
	"""Enable In Front"""
	bl_label="Enable In Front"
	bl_idname="object.enable_in_front"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_in_front = True
		return{'FINISHED'}

class Disable_In_Front(Operator):
	"""Disable In Front"""
	bl_label="Disable In Front"
	bl_idname="object.disable_in_front"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
		
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_in_front= False
		return{'FINISHED'}












registerable_classes=[]

for name in  inspect.getmembers(sys.modules[__name__],inspect.isclass):		
	cls = getattr(sys.modules[__name__],name[0])
	if getattr(cls,"bl_label",False):
		registerable_classes.append(cls)

def register():
	for cls in registerable_classes:
		if not getattr(cls,"is_registered",False):
			bpy.utils.register_class(cls)

def unregister():
	for cls in reversed(registerable_classes):
		if getattr(cls,"is_registered",False):
			bpy.utils.unregister_class(cls)

if __name__ == "__main__":
	register()

