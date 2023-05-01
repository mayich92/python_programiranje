from PIL import Image
from PIL import ImageFilter
from PIL import ImageEnhance
# from PIL import Image, ImageFilter

img = Image.open('Fotografije/Algebra_campus.jpg')

# img = img.filter(ImageFilter.CONTOUR)
# img = img.filter(ImageFilter.EDGE_ENHANCE)
# img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
# img = img.filter(ImageFilter.EMBOSS)
# img = img.filter(ImageFilter.FIND_EDGES)
# img = img.filter(ImageFilter.SHARPEN)
# img = img.filter(ImageFilter.SMOOTH)
# img = img.filter(ImageFilter.SMOOTH_MORE)

# help(ImageFilter.BoxBlur)
# img = img.filter(ImageFilter.BoxBlur(radius=10))
# img = img.filter(ImageFilter.GaussianBlur(radius=8))

# img = img.filter(ImageFilter.UnsharpMask(radius=7, percent=250, threshold=3))
# img = img.filter(ImageFilter.MaxFilter(size=7))
# img = img.filter(ImageFilter.MedianFilter(size=7))
# img = img.filter(ImageFilter.MinFilter(size=7))

# img_enhancer = ImageEnhance.Brightness(img)

# img_enhancer.enhance(2).show()

img_enhancer = ImageEnhance.Contrast(img)

img_enhancer.enhance(4).show()

# img_enhancer = ImageEnhance.Sharpness(img)
# img_enhancer = ImageEnhance.Color(img)
