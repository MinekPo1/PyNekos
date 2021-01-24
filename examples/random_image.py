"""
File that exemplify the use of the client to get a json with informations about random images.
"""

from PyNekos.nekosapi import Neko

nyan = Neko()
safe_kw = {
    'nsfw': False,
    'count': 2
}
sfw_images_json = nyan.random_image(**safe_kw)
print(sfw_images_json)

notsafe_kw = {
    'nsfw': True,
    'count': 2
}
nsfw_images_json = nyan.random_image(**notsafe_kw)
print(nsfw_images_json)


"""
Return:
{'images': [{'nsfw': False, 'tags': ['1 girl', 'animal ears', 'black legwear', 'black skirt', 'blue eyes', 'blush', 'cat ears', 'cat tail', 'cropped legs', 'fang', 'fang out', 'glasses', 'hands in pockets', 'hood', 'hood down', 'hooded jacket', 'hoodie', 'jacket', 'light brown hair', 'long hair', 'long sleeves', 'looking at viewer', 'original', 'pantyhose', 'red-framed eyewear', 'semi-rimless eyewear', 'simple background', 'sketch', 'skirt', 'smile', 'solo', 'tail', 'under-rim eyewear', 'white background'], 'likes': 4, 'favorites': 1, 'id': 'BJ8erxX2f', 'originalHash': '297fb4306ab442bcd6cdc0561934bbbb', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'shone', 'comments': [], 'createdAt': '2018-04-17T04:15:42.405Z', 'url': 'https://nekos.moe/image/BJ8erxX2f', 'thumbnail': 'https://nekos.moe/thumbnail/BJ8erxX2f'}, {'nsfw': False, 'tags': ['1 girl', 'anchor symbol', 'animal ears', 'bikini', 'bracelet', 'cat ears', 'cup', 'drinking glass', 'drinking straw', 'floating', 'flower', 'food', 'fruit', 'hair flower', 'hair ornament', 'hibiscus', 'holding', 'holding drinking glass', 'ice', 'ice cube', 'innertube', 'jewelry', 'long hair', 'mimiko (shibainu niki)', 'one eye closed', 'original', 'partially submerged', 'pink hair', 'purple eyes', 'smile', 'swimsuit', 'tropical drink', 'twintails', 'water'], 'likes': 4, 'favorites': 1, 'id': 'rkOSZMV3z', 'originalHash': 'e5643293f8d18173e1d799c632481f51', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'shibainu niki', 'comments': [], 'createdAt': '2018-04-18T00:28:48.207Z', 'url': 'https://nekos.moe/image/rkOSZMV3z', 'thumbnail': 'https://nekos.moe/thumbnail/rkOSZMV3z'}]}

{'images': [{'nsfw': True, 'tags': ['1 girl', 'animal ears', 'bell', 'bell choker', 'blue eyes', 'blush', 'bra', 'cat ears', 'cat lingerie', 'collar', 'eyebrows visible through hair', 'hibiki (kantai collection)', 'jingle bell', 'kantai collection', 'kemonomimi mode', 'kneeling', 'long hair', 'looking at viewer', 'meme attire', 'navel', 'panties', 'paw pose', 'paw print', 'shadow', 'side-tie panties', 'silver hair', 'solo', 'underwear'], 'likes': 3, 'favorites': 2, 'id': 'HkPomMGCz', 'originalHash': 'c978bc501360ac10d20f238a13119864', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'huwali (dnwls3010)', 'comments': [], 'createdAt': '2018-05-10T18:46:55.624Z', 'url': 'https://nekos.moe/image/HkPomMGCz', 'thumbnail': 'https://nekos.moe/thumbnail/HkPomMGCz'}, {'id': 'Hy3sLfoiW', 'originalHash': 'fa53e07f3e54ca7d937102ca9664ac91', 'uploader': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'gyuunyuukeepaa', 'tags': ['1girl', 'animal ears', 'armpits', 'blush', 'breasts', 'brown hair', 'closed eyes', 'corinne (shironeko project)', 'fang', 'long hair', 'nature', 'navel', 'nipples', 'nude', 'pond', 'shironeko project', 'simple background', 'small breasts', 'smile', 'solo', 'tail', 'tree', 'very long hair', 'white background'], 'comments': [], 'favorites': 6, 'likes': 13, 'nsfw': True, 'createdAt': '2017-09-29T00:41:08.986Z', 'url': 'https://nekos.moe/image/Hy3sLfoiW', 'thumbnail': 'https://nekos.moe/thumbnail/Hy3sLfoiW'}]}
"""