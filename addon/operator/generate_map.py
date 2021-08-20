import bpy


class CPK_OP_Generate_Map(bpy.types.Operator):

    """Generate packed texture"""

    bl_idname = "cpk.generate_map"
    bl_label = "Generate Map"

    @classmethod
    def poll(cls, context):
        chlCheck = context.scene.cpk_user_props

        red = chlCheck.red and chlCheck.redTextPath
        green = chlCheck.green and chlCheck.greenTextPath
        blue = chlCheck.blue and chlCheck.blueTextPath
        alpha = chlCheck.alpha and chlCheck.alphaTextPath

        if(red and green):
            return True

        if(red and blue):
            return True

        if(red and alpha):
            return True

        if(green and blue):
            return True

        if(green and alpha):
            return True

        if(blue and alpha):
            return True

        return False

    def execute(self, context):

        print('po')
        return {'FINISHED'}
