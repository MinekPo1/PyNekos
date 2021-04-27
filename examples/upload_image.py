"""
File that exemplify the use of the client to post a image to the Nekos.moe website.
"""

from PyNekosOO import *

nyan = Neko(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Danbooru post
dan_kw = {
    'image': '2613483',
    'upload_type': 'danbooru',
    'nsfw': False
}
danbooru = nyan.upload_image(**dan_kw)
print(danbooru)

# Local post
local_kw = {
    'image': 'neko.jpg',
    'image_path': '/home/user/path/to/image/neko.jpg',
    'upload_type': 'local',
    'tags': ['student'],
    'nsfw': False
}
local = nyan.upload_image(**local_kw)
print(local)

# Url post
url_kw = {
    'type':'link',
    'image': 'https://ih1.redbubble.net/image.608339956.2125/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
    'upload_type': 'url',
    'tags': ['animal ear', 'test'],
    'nsfw': False
}
url = nyan.upload_image(**url_kw)
print(url)