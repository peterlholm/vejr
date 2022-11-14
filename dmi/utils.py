"Div img utils"
from PIL import Image
import numpy as np

def convert_png_transparent(src_file, dst_file, bg_color=(0,0,0)):
    "Convert alle pixels with bg_color to transparant"
    image = Image.open(src_file).convert("RGBA")
    array = np.array(image, dtype=np.ubyte)
    mask = (array[:,:,:3] == bg_color).all(axis=2)
    alpha = np.where(mask, 0, 255)
    array[:,:,-1] = alpha
    Image.fromarray(np.ubyte(array)).save(dst_file, "PNG")

def convert_img_transparent(img, bg_color=(0,0,0)):
    "Convert alle pixels with bg_color to transparant from image"
    #image = Image.open(src_file).convert("RGBA")
    array = np.array(img, dtype=np.ubyte)
    mask = (array[:,:,:3] == bg_color).all(axis=2)
    alpha = np.where(mask, 0, 255)
    array[:,:,-1] = alpha
    return Image.fromarray(np.ubyte(array))

def get_img_tags(file):
    "return the tags as dict"
    img=Image.open(file)
    img.load()
    info = img.info
    return info
