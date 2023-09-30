from PIL import Image, ImageOps, ImageColor
import numpy as np

def grayscale(fp:str):
    file, suff = fp.rsplit(sep=".",maxsplit=1)
    with Image.open(fp=fp) as img:
        img = ImageOps.grayscale(img)
        img.save(file + "_grayscaled." + suff)

def invert(fp:str):
    file, suff = fp.rsplit(sep=".",maxsplit=1)
    with Image.open(fp=fp) as img:
        img = ImageOps.invert(img)
        img.save(file + "_inverted." + suff)

def remove_background(fp:str, sensitivity:float = 0.0, bg_color:np.array = np.array([255,255,255,255])):
        file, suff = fp.rsplit(sep=".",maxsplit=1)
        with Image.open(fp=fp) as img:
            img = img.convert("RGBA")
            imgarr = np.array(img)

            #Sensitivity range
            lower = bg_color - (bg_color * sensitivity)
            upper = bg_color + (bg_color * sensitivity)
            imgarr = np.where(np.all(imgarr <= upper, axis=-1,keepdims=True) & np.all(imgarr >= lower, axis=-1,keepdims=True), 0, imgarr)
            
            #imgarr = np.where(imgarr[:,:,0] == bg_color[0] and imgarr[:,:,1] == bg_color[1] and imgarr[:,:,2] == bg_color[2] and imgarr[:,:,3] == bg_color[3], imgarr, 0)
            Image.fromarray(imgarr).save(file +"_no_background.png")

def rgba_to_hex(rgba:np.array) -> str:
     r = hex(rgba[0])[2:]
     g = hex(rgba[1])[2:]
     b = hex(rgba[2])[2:]
     a = hex(rgba[3])[2:]
     hex_string = "#"
     for val in (r,g,b,a):
        if(len(val) == 1):
            hex_string += (f"0{val}")
        else:
             hex_string += val
     return hex_string

remove_background("C:\\Users\\jacob\\Downloads\\Untitled.jpg", 0.8)