from PIL import Image, ImageOps
def to_png(fp:str):
    file = fp.rsplit(sep=".",maxsplit=1)[0]
    with Image.open(fp=fp) as img:
        img.save(file + ".png")

def to_jpg(fp:str):
    file = fp.rsplit(sep=".",maxsplit=1)[0]
    with Image.open(fp=fp) as img:
        img = img.convert("RGB")
        img.save(file + ".jpg")

def to_bmp(fp:str):
    file = fp.rsplit(sep=".",maxsplit=1)[0]
    with Image.open(fp=fp) as img:
        img.save(file + ".bmp")