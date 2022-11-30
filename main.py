from PIL import Image, ImageEnhance

im = Image.open("image.jpg")

enhancer = ImageEnhance.Contrast(im)

factor = 1
im_output = enhancer.enhance(factor)
im_output.save('original-image.png')

factor = 0.5
im_output = enhancer.enhance(factor)
im_output.save('less-contrast-image.png')

factor = 1.5
im_output = enhancer.enhance(factor)
im_output.save('more-contrast-image.png')