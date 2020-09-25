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

import sys,inspect
import bpy
from bpy.types import Panel



Preferences=bpy.context.preferences

class VIEW3D_PT_fast_toggle_preferences(Panel):
	bl_label="Preferences"
	bl_space_type='VIEW_3D'
	bl_region_type='UI'
	bl_category="Fast Toggle"
	bl_options={'DRAW_BOX','DEFAULT_CLOSED'}

	def draw(self,context):
		Layout=self.layout
		Col=Layout.column(align=True)
		Col.label(text="Interface")
		Col.prop(Preferences.view,"ui_scale")
		Col.separator()
		Col.row(align=True).prop(Preferences.view,"ui_line_width",expand=True)
		
		Col=Layout.column(align=True)
		Col.label(text="System")
		Col.prop(Preferences.edit,"undo_steps")

		Col=Layout.column(align=True)
		Col.label(text="Viewport")
		Col.prop(Preferences.system,"viewport_aa",text="")
		Col.separator()
		Col.prop(Preferences.view,"gizmo_size")

		Col=Layout.column(align=True)
		Col.label(text="Align New Object To")
		Col.row(align=True).prop(Preferences.edit,"object_align",expand=True)
		Col.prop(Preferences.edit,"use_enter_edit_mode")

		Col=Layout.column(align=True)
		Col.label(text="Orbit Method")
		Col.row(align=True).prop(Preferences.inputs,"view_rotate_method",expand=True)
		Row=Col.row(align=True)
		Row.prop(Preferences.inputs,"use_mouse_depth_navigate")
		Row.prop(Preferences.inputs,"use_rotate_around_active")

class VIEW3D_PT_fast_toggle_object(Panel):
	bl_label="Object"
	bl_space_type='VIEW_3D'
	bl_region_type='UI'
	bl_category="Fast Toggle"
	bl_options={'DRAW_BOX','DEFAULT_CLOSED'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D')



	def draw(self,context):
		Layout=self.layout
		Col=Layout.column(align=True)
		Row=Col.row(align=True,heading="Change")
		Row.prop(context.scene.fast_toggle,"operation_upon",expand=True)
		Col.separator()
		Row=Col.row(align=True)
		Row.operator("object.set_display_as_wire",text="Wire")
		Row.operator("object.set_display_as_textured",text="Textured")
		Row.operator("object.set_display_as_solid",text="Solid")
		Col.separator()
		Row=Col.row(align=True)
		Row.operator("object.set_bounds_display_sphere",text="Sphere")
		Row.operator("object.set_bounds_display_cone",text="Cone")
		Row.operator("object.set_bounds_display_box",text="Box")
		
		Row=Col.row(align=True)
		Row.operator("object.set_bounds_display_cylinder",text="Cylinder")
		Row.operator("object.set_bounds_display_capsule",text="Capsule")
		Row.operator("object.disable_bounds_display",text="None")
		
		Col.separator()
		Row=Col.row(align=True)
		Row.label(text="Wire")
		Row.operator("object.enable_wireframe",text="ON")
		Row.operator("object.disable_wireframe",text="OFF")
		Row.label(text="Name")
		Row.operator("object.show_name",text="ON")
		Row.operator("object.hide_name",text="OFF")

		Col.separator()
		Row=Col.row(align=True)
		Row.label(text="Axis")
		Row.operator("object.enable_axis",text="ON")
		Row.operator("object.disable_axis",text="OFF")
		Row.label(text="Depth")
		Row.operator("object.enable_in_front",text="+VE")
		Row.operator("object.disable_in_front",text="-VE")

class VIEW3D_PT_fast_toggle_viewport(Panel):
	bl_label="Viewport"
	bl_space_type='VIEW_3D'
	bl_region_type='UI'
	bl_category="Fast Toggle"
	bl_options={'DRAW_BOX','DEFAULT_CLOSED'}

	@classmethod
	def poll(cls,context):
		return (context.space_data.type == 'VIEW_3D')

	def draw(self,context):
		pass



class VIEW3D_PT_fast_toggle_viewport_guides(Panel):
	bl_label="Guides and Text and Infos"
	bl_space_type='VIEW_3D'
	bl_region_type='UI'
	bl_category="Fast Toggle"
	bl_parent_id="VIEW3D_PT_fast_toggle_viewport"

	def draw(self,context):
		Layout=self.layout
		Col=Layout.column(align=True)
		Row=Col.row(align=True,heading="Guides")
		Row.prop(context.space_data.overlay,"show_ortho_grid",text="Grid",toggle=True)
		Row.prop(context.space_data.overlay,"show_floor",text="Floor",toggle=True)
		Col.separator()
		Row=Col.row(align=True)
		Row.prop(context.space_data.overlay,"show_axis_x",text="X",toggle=True)
		Row.prop(context.space_data.overlay,"show_axis_y",text="Y",toggle=True)
		Row.prop(context.space_data.overlay,"show_axis_z",text="Z",toggle=True)
		Col.separator()
		Row=Col.row(align=True)
		Row.prop(context.space_data.overlay,"show_text",text="Text",toggle=True)
		Row.prop(context.space_data.overlay,"show_stats",text="Stats",toggle=True)
		
		Row=Col.row(align=True)
		Row.prop(context.space_data.overlay,"show_cursor",text="3D Cursor",toggle=True)
		Row.prop(context.space_data.overlay,"show_annotation",text="Annotation",toggle=True)
		
class VIEW3D_PT_fast_toggle_viewport_shading(Panel):
	bl_label="Shading"
	bl_space_type='VIEW_3D'
	bl_region_type='UI'
	bl_category="Fast Toggle"
	bl_parent_id="VIEW3D_PT_fast_toggle_viewport"

	def draw(self,context):
		Layout=self.layout
		Col=Layout.column(align=True)
		Col.label(text="Shading Color")
		Col.grid_flow(columns=3,align=True).prop(context.space_data.shading,"color_type",expand=True)		
		
		if context.selected_objects and context.space_data.shading.color_type=="OBJECT":
			Col.separator()
			if len(context.selected_objects)==1:
				Col.prop(context.object,"color",text="")
			else:
				Col.prop(context.scene.fast_toggle,"object_color")
		if context.space_data.shading.color_type=="SINGLE":
			Col.separator()
			Col.prop(context.space_data.shading,"single_color",text="")
		


registerable_classes=[
	VIEW3D_PT_fast_toggle_preferences,
	VIEW3D_PT_fast_toggle_object,
	VIEW3D_PT_fast_toggle_viewport,
]


for name in  inspect.getmembers(sys.modules[__name__],inspect.isclass):		
	cls = getattr(sys.modules[__name__],name[0])
	if getattr(cls,"bl_label",False):
		if cls in registerable_classes:
			pass
		
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