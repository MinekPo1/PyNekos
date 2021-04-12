"""
File that exemplify the use of the client to get the link of the image using a ID.
"""

from PIL import Image
from PyNekos import nekosapi

#old:
nyan = nekosapi.Neko()
image_link = nyan.get_link('Sy9sHFa8X')
print(image_link)

"""
Return:
https://nekos.moe/image/Sy9sHFa8X
"""

#the new version does not have this type of shortcut.
#instead you can directly download the image

image = nekosapi.Post('Sy9sHFa8X')
img = image.get_image()

#it is stored in a file like format, which means you can easley load it:

Image.open(img).show()

# if you run this code you should see a catgirl pop up.