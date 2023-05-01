from PIL import Image

# učitavanje slike
filepath = 'Algebra_campus.jpg'
img = Image.open(filepath)

# određivanje regije za cenzuriranje
box = (0, 0, 100, 100)
region = img.crop(box)

# primjena efekta zamućivanja na regiju
factor = 10
blurred = region.resize((region.width // factor, region.height // factor), resample=Image.BOX)
blurred = blurred.resize(region.size, resample=Image.BOX)

# vraćanje regije s efektom zamućivanja na iste koordinate u originalnoj slici
img.paste(blurred, box)

# spremanje izmijenjene slike
img.save("output.jpg")
