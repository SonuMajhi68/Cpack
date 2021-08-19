import bpy

from .generate_map import CPK_OP_Generate_Map


classes = (
    CPK_OP_Generate_Map,
)


def register_operator():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)


def unregister_operator():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)
