# install packages.
# pip install pyqrcode
# pip install pypng

import pyqrcode
data = 'nishantsingh70.com'
img = pyqrcode.create(data)

img.png('blogwebsite.png', scale = 10)
