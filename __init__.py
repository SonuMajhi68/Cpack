bl_info = {
    "name": "Cpack",
    "description": "Channel packing tool",
    "author": "Sonu Majhi",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D",
    "category": "3D View"
}


def register():
    from .addon.register import register_addon
    register_addon()


def unregister():
    from . addon.register import unregister_addon
    unregister_addon()
