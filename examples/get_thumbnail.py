"""
File that exemplify the use of the client to get the link of the image thumbnail using a ID.
"""

from PIL import Image
from PyNekos import nekosapi

#Old:
nyan = nekosapi.Neko()
thumb_link = nyan.get_thumbnail('Sy9sHFa8X')
print(thumb_link)

"""
Return:
https://nekos.moe/thumbnail/Sy9sHFa8X
"""

#New will return a file like object similarly to Post.get_image()

image = nekosapi.Post('Sy9sHFa8X')
img = image.get_thumbnail()

Image.open(img).show()