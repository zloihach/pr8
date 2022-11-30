from PIL import Image, ImageEnhance, ImageOps

#read the image
im = Image.open("image.jpg")

#image brightness enhancer
enhancer = ImageEnhance.Brightness(im)

#image invert color enhancer
im = Image.open('image.jpg')
im_invert = ImageOps.invert(im)
im_invert.save('invert.jpg', quality=95)

# factor = 1 #gives original image
# im_output = enhancer.enhance(factor)
# im_output.save('original-image.png')
#
# factor = 0.5 #darkens the image
# im_output = enhancer.enhance(factor)
# im_output.save('darkened-image.png')
#
# factor = 1.5 #brightens the image
# im_output = enhancer.enhance(factor)
# im_output.save('brightened-image.png')