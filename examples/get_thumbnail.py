"""
File that exemplify the use of the client to get the link of the image thumbnail using a ID.
"""

from PyNekos import nekosapi

nyan = nekosapi.Neko()
thumb_link = nyan.get_thumbnail('Sy9sHFa8X')
print(thumb_link)


"""
Return:
https://nekos.moe/thumbnail/Sy9sHFa8X
"""