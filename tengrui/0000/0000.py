from PIL import Image, ImageDraw, ImageFont

image = Image.open('head_400.jpg')
width, high = image.size
draw = ImageDraw.Draw(image)
num = '4'

# use a truetype font
font = ImageFont.truetype('arial.ttf', int(width / 3))
draw.text((width - width / 3, 0), num, fill=(255, 0, 0), font=font)

image.save('result.jpg', 'jpeg')
image.show()

# https://pillow.readthedocs.io/en/3.1.x/reference/ImageFont.html#module-PIL.ImageFont
