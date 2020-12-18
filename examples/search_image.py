"""
File that exemplify the use of the client to get a json with informations using the search to filter images.
"""

from PyNekos.nekosapi import Neko

nyan = Neko()
search_json = nyan.search_image(nsfw=False, uploader='brussell', artist='jun', tags=["1 girl", "animal ears"], sort='likes')
print(search_json)

# Search for images posted after 30/11/2019
search_json2 = nyan.search_image(nsfw=False, posted_after="2019.11.30")
print(search_json2)

# Search for images posted before 30/11/2020
search_json3 = nyan.search_image(nsfw=False, posted_before="2020.11.30")
print(search_json3)

"""
Return:
{'images': [{'id': 'r1MekJKUG', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'juna', 'comments': [], 'favorites': 1, 'likes': 2, 'tags': ['1 girl', ':<', 'animal ears', 'bag', 'bangs', 'black blazer', 'black hair', 'black skirt', 'blazer', 'blue eyes', 'blue sky', 'blush', 'bookbag', 'bow', 'bowtie', 'cardigan', 'cat ears', 'cat girl', 'cat tail', 'closed mouth', 'cloud', 'cloudy sky', 'collarbone', 'collared shirt', 'day', 'eyebrows visible through hair', 'head tilt', 'jacket', 'long hair', 'long sleeves', 'open blazer', 'open clothes', 'open jacket', 'outdoors', 'plaid', 'plaid skirt', 'pleated skirt', 'railing', 'red neckwear', 'road sign', 'school bag', 'school uniform', 'shirt', 'sign', 'sitting', 'skirt', 'sky', 'sleeves past wrists', 'solo', 'tail', 'white shirt', 'original', 'letter'], 'nsfw': False, 'createdAt': '2018-02-07T20:17:46.763Z', 'url': 'https://nekos.moe/image/r1MekJKUG', 'thumbnail': 'https://nekos.moe/thumbnail/r1MekJKUG'}, {'nsfw': False, 'tags': [':o', '1 girl', 'ahoge', 'animal ears', 'bangs', 'bed', 'bed sheet', 'black hair', 'black jacket', 'black legwear', 'blue eyes', 'blush', 'cat ears', 'cat girl', 'cat tail', 'collared shirt', 'curtains', 'eyebrows visible through hair', 'full body', 'hair ribbon', 'indoors', 'jacket', 'kemonomimi mode', 'kneeling', 'long hair', 'long sleeves', 'looking at viewer', 'miniskirt', 'multicolored', 'multicolored clothes', 'multicolored skirt', 'neck ribbon', 'on bed', 'parted lips', 'paw pose', 'pleated skirt', 'red neckwear', 'red ribbon', 'ribbon', 'school uniform', 'shirt', 'skirt', 'sobu high school uniform', 'solo', 'straight hair', 'striped', 'tail', 'thighhighs', 'vertical stripes', 'vertical-striped skirt', 'very long hair', 'white shirt', 'yahari ore no seishun lovecome wa machigatteiru.', 'yukinoshita yukino', 'zettai ryouiki'], 'likes': 1, 'favorites': 0, 'id': 'GjS-oEacX', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'jun (aousa0328)', 'comments': [], 'createdAt': '2020-09-01T05:02:17.554Z', 'url': 'https://nekos.moe/image/GjS-oEacX', 'thumbnail': 'https://nekos.moe/thumbnail/GjS-oEacX'}]}
"""