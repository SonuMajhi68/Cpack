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

        from ..utility.image_processing import (validateImage, generatePixel)

        u_input = context.scene.cpk_user_props
        imgData = bpy.data.images

        imgs = []

        if u_input.red:
            imgRef = imgData.load(u_input.redTextPath)
            imgs.append(imgRef)
        if u_input.green:
            imgRef = imgData.load(u_input.greenTextPath)
            imgs.append(imgRef)
        if u_input.blue:
            imgRef = imgData.load(u_input.blueTextPath)
            imgs.append(imgRef)
        if u_input.alpha:
            imgRef = imgData.load(u_input.alphaTextPath)
            imgs.append(imgRef)

        if validateImage(imgs):
            width, height = imgs[0].size

            tex = imgData.new(name=u_input.name, width=width, height=height)
            tex_px = list(tex.pixels)

            tex.pixels[:] = generatePixel(imgs, tex_px, u_input)

        if not validateImage(imgs):
            self.report({'Error'}, 'Printing report to Info window.')

        return {'FINISHED'}
