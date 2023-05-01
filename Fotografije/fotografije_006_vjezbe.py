# Zadatak 29
# cenzurirati dio slike

from PIL import Image

filename = 'Fotografije/Algebra_campus.jpg'
img = Image.open(filename)

mask = (800, 500, 3400, 2200)

subimg = img.crop(mask)

width, height = subimg.size
original = (width, height)
degree = 50
width = round(width/degree)
height = round(height/degree)
subimg = subimg.resize((width, height), Image.LANCZOS)
subimg = subimg.resize(original, Image.LANCZOS)

img.paste(subimg, mask)

img.show()