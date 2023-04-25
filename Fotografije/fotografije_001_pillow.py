import os

os.chdir('Fotografije')

from PIL import Image

filepath = 'Algebra_campus.jpg'
# filepath = 'python-logo.png'
img = Image.open(filepath)
print(img.format)
print(img.mode)
print(img.size)
print(img.size[0])    # width/širina
print(img.size[1])    # height/visina

dimenzije_prozora = (0, 0, 1000, 1000)   # lijevo, gore, desno, dolje
width = img.size[0]
height = img.size[1]
prvi_kvadrant = (0, 0, width/2, height/2)

img = img.crop(prvi_kvadrant)

# za kasnije
# width /= 10
# height /= 10

# width = round(width)
# height = round(height)

# img.resize(width, height)

# img.show()

img = img.convert(mode='L')    # crno-bijeli filter

subimage = Image.open('it.jpg')
img.paste(subimage, (200, 200))

new_filepath = 'Algebra_crop.jpg'
img.save(new_filepath, 'JPEG')

img = Image.open('Algebra_campus.jpg')
# img.transpose(Image.FLIP_LEFT_RIGHT).show()
# Image.FLIP_TOP_BOTTOM
# Image.ROTATE_90
# Image.ROTATE_180
# Image.ROTATE_270
# Image.TRANSPOSE
# Image.TRANSVERSE