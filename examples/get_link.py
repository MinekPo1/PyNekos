"""
File that exemplify the use of the client to get the link of the image using a ID.
"""

from PyNekos.nekosapi import Neko

nyan = Neko()
image_link = nyan.get_link('Sy9sHFa8X')
print(image_link)


"""
Return:
https://nekos.moe/image/Sy9sHFa8X
"""