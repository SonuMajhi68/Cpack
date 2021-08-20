
def validateImage(imgs):
    reso = [imgs[0].size[0], imgs[0].size[1]]

    for img in imgs:
        i_reso = [img.size[0], img.size[1]]

        if reso != i_reso:
            return False

    return True


def generatePixel(imgs, tex, mytool):

    from .greyscale_method import (averageMethod, lumaMethod, desaturatMethod)

    img_Data = []

    for img in imgs:
        img_Data.append(list(img.pixels))

    for px in range(0, len(img_Data[0]), 4):
        if mytool.red:
            tex[px] = averageMethod(px, img_Data[0])

        if mytool.green:
            tex[px + 1] = averageMethod(px, img_Data[1])

        if mytool.blue:
            tex[px + 2] = averageMethod(px, img_Data[2])

        if mytool.alpha:
            tex[px + 3] = averageMethod(px, img_Data[3])

#            tex[px] = img[px]

    return tex
