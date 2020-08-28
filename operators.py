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

# A dictionary for Obj Name and their Display Type	
original_display_type={}


##########_____ DISPLAY TYPE RELATED _____##########

class Set_Display_As_Bounds(Operator):
	"""Set 'Bounds' display method for the selected object"""
	bl_label="Set Bounds Display Type"
	bl_idname="object.set_display_as_bounds"
	bl_options={'REGISTER','UNDO'}
	
	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):	
		for obj in context.selected_objects:	
			# Add the obj name and it's display type to a dictionary					
			original_display_type[obj.name]=obj.display_type			
			obj.display_type = 'BOUNDS'
		print(original_display_type)
		return{'FINISHED'}

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
			# Add the obj name and it's display type to a dictionary				
			original_display_type[obj.name]=obj.display_type			
			obj.display_type = 'WIRE'
		print(original_display_type)
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
			# Add the obj name and it's display type to a dictionary					
			original_display_type[obj.name]=obj.display_type			
			obj.display_type = 'SOLID'
		print(original_display_type)
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
			# Add the obj name and it's display type to a dictionary				
			original_display_type[obj.name]=obj.display_type			
			obj.display_type = 'TEXTURED'
		print(original_display_type)
		return{'FINISHED'}




##########_____ BOUNDS RELATED _____##########

class Set_Bounds_Display_Box(Operator):
	"""Set bounds display as 'BOX'"""
	bl_label="Set Bounds Display -> Box"
	bl_idname="object.set_bounds_display_box_xxx"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)

	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = True
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
			obj.display_bounds_type = 'CAPSULE'

		return{'FINISHED'}

class Disable_Bounds_Display(Operator):
	"""Disable bounds display"""
	bl_label="Disable Bounds Display"
	bl_idname="object.disable_bounds_display_asd"
	bl_options={'REGISTER','UNDO'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D'
		and context.selected_objects)
	
	def execute(self,context):
		for obj in context.selected_objects:
			obj.show_bounds = False
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

