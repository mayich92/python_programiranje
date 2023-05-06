# Zadatak 30.
# napraviti PIL program koji na sve slike u zadanom dir postavlja watermark i sprema
# obrađene slike u odredišni dir
# bonus bodovi/istražiti: prozirnost watermarka

import os
from PIL import Image

os.chdir('GUI')

input_dir = 'input_dir'
dest_dir = 'dest_dir'
watermark_filepath = 'python-logo.png'
coordinates = (100, 100)
TRANSPARENCY = 50

files = os.listdir(input_dir)
input_images = []
valid_extensions = ['jpg', 'png', 'bmp', 'tif', 'tiff', 'gif']
for file in files:
    extension = file.split('.')[-1]
    if extension in valid_extensions:
        input_images.append(file)
    # if file.endswith('.jpg') or file.endswith('.png'):
    #     input_images.append(file)

def put_watermark(filepath, watermark_path, fold, dest_filepath):
    img = Image.open(filepath)
    watermark = Image.open(watermark_path)
    width, height = watermark.size
    width = round(width/fold)
    height = round(height/fold)
    watermark = watermark.resize((width, height))
    watermark = watermark.convert(mode='RGBA')
    
    paste_mask = watermark.split()[3].point(lambda i: i * TRANSPARENCY / 100.)
    # watermark.split() -> razdvaja sliku na kanale -> ako je RGBA -> 4 kanala
    # [3] -> uzimamo zadnji kanal
    # .point() -> mapira funkciju na sve vrijednosti slike (kanala)
    # lambda funkcija -> kraći oblik funkcije -> svaka vrijednost i se postavlja na modificirani i
    # modificirani i = i * TRANSPARENCY / 100

    img.paste(watermark, coordinates, mask=paste_mask)
    img.save(dest_filepath, 'JPEG')

fold = 12
# print(input_images)
for image_path in input_images:
    filepath = os.path.join(input_dir, image_path)
    dest = os.path.join(dest_dir, image_path)
    put_watermark(filepath, watermark_filepath, fold, dest)

'''
https://stackoverflow.com/a/50981314

TRANSPARENCY = 65       # percentage

temp_image = Image.open('test1.jpg')
watermark = Image.open('watermark.png')    

if watermark.mode!='RGBA':
    alpha = Image.new('L', watermark.size, 255)
    watermark.putalpha(alpha)

paste_mask = watermark.split()[3].point(lambda i: i * TRANSPARENCY / 100.)
temp_image.paste(watermark, (0,0), mask=paste_mask)
temp_image.save('res.png')
'''