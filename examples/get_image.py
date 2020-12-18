"""
File that exemplify the use of the client to get a json with informations about a ID of a image.
"""

from PyNekos import nekosapi

nyan = nekosapi.Neko()
image_json = nyan.get_image('Sy9sHFa8X')
print(image_json)


"""
Return:
{'image': {'nsfw': False, 'tags': ['1girl', 'animal ears', 'bangs', 'blush', 'cat ears', 'cat tail', 'covering mouth', 'eyebrows visible through hair', 'eyes visible through hair', 'grey background', 'hair between eyes', 'hair ribbon', 'head tilt', 'heterochromia', 'looking at viewer', 'nagishiro mito', 'original', 'pink hair', 'red eyes', 'ribbon', 'simple background', 'sleeves past fingers', 'sleeves past wrists', 'solo', 'tail', 'upper body', 'virtual youtuber', 'yellow eyes'], 'likes': 2, 'favorites': 2, 'id': 'Sy9sHFa8X', 'uploader': {'id': 'Bk8easipZ', 'username': 'kurozero'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'nagishiro mito', 'comments': [], 'createdAt': '2018-08-24T13:18:26.498Z', 'url': 'https://nekos.moe/image/Sy9sHFa8X', 'thumbnail': 'https://nekos.moe/thumbnail/Sy9sHFa8X'}}
"""