from PIL import Image, ImageFilter

img = Image.open('./astro.jpeg')
img.thumbnail((400, 400))
img.save("thumbnail.jpeg", 'jpeg')
print(img.size)