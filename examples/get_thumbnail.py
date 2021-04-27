"""
Getting thumbnail file and showing it using PIL
"""

from PIL import Image
from PyNekosOO import *

#Will return a file like object similarly to Post.get_image()

image = Post('Sy9sHFa8X')
img = image.get_thumbnail()

Image.open(img).show()