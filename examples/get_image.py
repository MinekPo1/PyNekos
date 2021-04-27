"""
Getting image file and showing it using PIL
"""

from PIL import Image
from PyNekosOO import *

image = Post('Sy9sHFa8X')
img = image.get_image()

#the image is stored in a file like format, which means you can easley load it:

Image.open(img).show()

# if you run this code you should see a catgirl pop up.