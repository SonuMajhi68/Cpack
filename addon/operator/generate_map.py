import bpy


class CPK_OP_Generate_Map(bpy.types.Operator):

    """Generate packed texture"""

    bl_idname = "cpk.generate_map"
    bl_label = "Generate Map"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        print('po')
        return {'FINISHED'}
