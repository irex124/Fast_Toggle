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
from bpy.props import BoolProperty,PointerProperty,EnumProperty,FloatVectorProperty
from bpy.types import PropertyGroup

def update_color(self,context):
    for obj in context.selected_objects:
        obj.color=context.scene.fast_toggle.object_color
    


class Fast_Toggle_Properties(PropertyGroup):
    operation_upon : EnumProperty(
        items = [("object", "Object", "", 1),
                 ("bounds", "Bounds", "", 2)],
        description="Whether to change the object's bounds or the object itself",
        )
    object_color: FloatVectorProperty(
        name="",
        subtype='COLOR',
        size=4,
        max=1,
        min=0,
        default=[1.0,1.0,1.0,1.0],
        update=update_color,
        description="Change the color of the objects"
        )


classes=[Fast_Toggle_Properties]
def register():
    for cls in classes:
        if not getattr(cls,"is_registered",False):
            bpy.utils.register_class(cls)
    bpy.types.Scene.fast_toggle=PointerProperty(type=Fast_Toggle_Properties)

def unregister():
    bpy.utils.unregister_class(Fast_Toggle_Properties)
    del bpy.types.Scene.fast_toggle
