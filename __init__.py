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

bl_info = {
    "name" : "Fast Toggle",
    "author" : "Pasang Bomjan",
    "description" : "A simple addon to quickly quickly set/enable/disable/toggle various options in blender.",
    "blender" : (2, 90, 0),
    "version" : (1, 0, 0),
    "location" : "View 3D > Sidebar > Fast Toggle",
    "warning" : "",
    "category" : "Generic"
}

if not "bpy" in locals():
    from . import (properties,operators,panels)
else:
    from importlib import reload
    reload(properties)
    reload(operators)
    reload(panels)
    del reload
    
import bpy

def register():
    properties.register()
    operators.register()
    panels.register()
def unregister():
    properties.unregister()
    operators.unregister()
    panels.register()

if __name__ == "__main__":
    register()



