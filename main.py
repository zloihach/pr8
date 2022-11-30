from PIL import Image, ImageOps

# open image
img = Image.open("image.jpg")

# border color
color = "green"

# top, right, bottom, left
border = (10, 10, 10, 10)

new_img = ImageOps.expand(img, border=border, fill=color)

# save new image
new_img.save("border.jpg")

