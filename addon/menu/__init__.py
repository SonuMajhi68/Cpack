import bpy
from bpy.props import PointerProperty

from .input_class import CPK_MU_User_Input
from .side_bar_panel import CPK_PT_Panel


classes = (
    CPK_MU_User_Input,
    CPK_PT_Panel,
)


def register_menu():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bpy.types.Scene.cpk_user_props = PointerProperty(
        type=CPK_MU_User_Input)


def unregister_menu():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.cpk_user_props
