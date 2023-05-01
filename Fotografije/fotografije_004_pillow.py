from PIL import Image, ImageDraw

img = Image.open('Fotografije/Algebra_campus.jpg')

img_draw = ImageDraw.Draw(img)

coordinates = (200, 200, 2000, 2000)
img_draw.rectangle(coordinates, fill=None, outline='green', width=50)

img_draw.ellipse(coordinates, fill=None, outline='red', width=5)

img.show()