#! python

#Install the library
#pip install captcha

# Import the necessary module
from captcha.image import ImageCaptcha

# Store and define dimentions
image = ImageCaptcha(width=280, height=90)

#Define data
data = image.generate("HelloWorld")

#Write to the file
image.write("HelloWorld", "ImageCaptcha.png")

