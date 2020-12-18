"""
File that exemplify the use of the client to post a image to the Nekos.moe website.
"""

from PyNekos.nekosapi import Neko

nyan = Neko(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Danbooru post
danbooru = nyan.upload_image(image='2613483', upload_type='danbooru', nsfw=False)
print(danbooru)

# Local post
local = nyan.upload_image(image='neko.jpg', image_path='/home/user/path/to/image/neko.jpg', upload_type='local', tags=['student'], nsfw=False)
print(local)

# Url post
url = nyan.upload_image(image='https://ih1.redbubble.net/image.608339956.2125/flat,750x,075,f-pad,750x1000,f8f8f8.jpg', upload_type='url', tags=['animal ear', 'test'], nsfw=False)
print(url)


"""
Return:
Danbooru - {'image': {'id': 'U02hHyznr', 'createdAt': '2020-12-15T17:01:27.493Z', 'uploader': {'id': 'WwK11x1jv', 'username': 'ChoiYun'}, 'tags': ['1girl', 'animal', 'animal ears', 'bangs', 'blue eyes', 'blush', 'bow', 'bunny', 'chestnut mouth', 'claw pose', 'day', 'dress', 'ears', 'fang', 'hand up', 'holding', 'holding animal', 'log cabin', 'long hair', 'looking at viewer', 'nature', 'open mouth', 'outdoors', 'parody', 'ponytail', 'signature', 'silver hair', 'solo', 'tail', 'wolf ears', 'wolf tail'], 'artist': 'chinomaron', 'nsfw': False}, 'image_url': 'https://nekos.moe/image/U02hHyznr.jpg', 'post_url': 'https://nekos.moe/post/U02hHyznr'}

Local - {'image': {'id': '5WUfMNr7j', 'createdAt': '2020-12-15T17:00:41.440Z', 'uploader': {'id': 'WwK11x1jv', 'username': 'ChoiYun'}, 'tags': ['student'], 'nsfw': False}, 'image_url': 'https://nekos.moe/image/5WUfMNr7j.jpg', 'post_url': 'https://nekos.moe/post/5WUfMNr7j'}

Url - {'image': {'id': 'JcsllehX-', 'createdAt': '2020-12-15T17:05:26.267Z', 'uploader': {'id': 'WwK11x1jv', 'username': 'ChoiYun'}, 'tags': ['animal ear', 'test'], 'nsfw': False}, 'image_url': 'https://nekos.moe/image/JcsllehX-.jpg', 'post_url': 'https://nekos.moe/post/JcsllehX-'}
"""