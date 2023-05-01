import os

from PIL import Image

os.chdir('Fotografije')

filepath = 'Algebra_campus.jpg'
# filepath = 'python-logo.png'
img = Image.open(filepath)
print(img.format)
print(img.mode)
print(img.size)
print(img.size[0])    # width/širina
print(img.size[1])    # height/visina

# img.show()

dimenzije_prozora = (1000, 1000, 2000, 1100)   # lijevo, gore, desno, dolje
width, height = img.size
lijevi_gornji_kvadrant = (0, 0, width/2, height/2)
desni_gornji_kvadrant = (width/2, 0, width, height/2)
lijevi_donji_kvadrant = (0, height/2, width/2, height)
desni_donji_kvadrant = (width/2, height/2, width, height)

# img = img.crop(desni_donji_kvadrant)
# img.show()

# width = 500
# height = 500

# degree = 0.1
# original = (width, height)
# width = round(width * degree)
# height = round(height * degree)

# img = img.resize((width, height))
# # img = img.resize((width, height), Image.LANCZOS)
# width, height = original
# img = img.resize((width, height))


# img = img.convert(mode='L')    # crno-bijeli filter
# img = img.convert('L')    # alternativno koristiti pozicijski argument -> identično


subimage = Image.open('python-logo.png')
subimage = subimage.resize((400, 400))
img.paste(subimage, (width - 200 - 400, height - 200 - 400))
# img.show()

# img.close()    # uništava img objekt i oslobađa memorija
new_filepath = 'Algebra_Python.jpg'
img.save(new_filepath, 'JPEG')

# img.transpose(Image.FLIP_LEFT_RIGHT).show()
# img.transpose(Image.FLIP_TOP_BOTTOM).show()
# img.transpose(Image.ROTATE_90).show()
# img.transpose(Image.ROTATE_180).show()
# img.transpose(Image.ROTATE_270).show()

# img.transpose(Image.FLIP_TOP_BOTTOM).transpose(Image.FLIP_LEFT_RIGHT).show()
# img.transpose(Image.TRANSPOSE).show()
# img.transpose(Image.TRANSVERSE).show()

