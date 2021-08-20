

def averageMethod(px, img):
    value = (img[px] + img[px + 1] + img[px + 2]) / 3
    return value


def lumaMethod(px, img):
    value = (img[px] * 0.3) + (img[px + 1] * 0.59) + (img[px + 2] * 0.11)
    return value


def desaturation(px, img):
    value = (max(img[px], img[px + 1], img[px + 2]) +
             min(img[px], img[px + 1], img[px + 2])) / 2
    return value


# other luma recommendation:-
# Gray = (Red * 0.3 + Green * 0.59 + Blue * 0.11)           gimp/photoshop
# Gray = (Red * 0.2126 + Green * 0.7152 + Blue * 0.0722)    BT.709
# Gray = (Red * 0.299 + Green * 0.587 + Blue * 0.114)       BT.601
