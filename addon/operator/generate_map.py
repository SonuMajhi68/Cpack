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
        from time import time

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

        t0 = time()

        if validateImage(imgs):
            width, height = imgs[0].size

            tex = imgData.new(name=u_input.name, width=width, height=height)
            tex_px = list(tex.pixels)

            tex.pixels[:] = generatePixel(imgs, tex_px, u_input)

        if not validateImage(imgs):
            self.report({'Error'}, 'Printing report to Info window.')

        print("Time spent: %s seconds" % (time() - t0))
        # print("Time spent: %S seconds" % ((datetime.now() - t0).total_seconds))
        # print(datetime.now().strftime("%S") - t0.strftime("%S"))

        return {'FINISHED'}
