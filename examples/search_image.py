"""
File that exemplify the use of the client to get a json with informations using the search to filter images.
"""

from PyNekos import nekosapi

search_kw = {
    'nsfw': False,
    'uploader': 'brussell',
    'tags': ['1 girl', 'animal ears'],
    'sort': 'likes',
    'posted_before': '2018.05.02',  # YYYY/MM/DD
    'limit': 10
}

#Old:
nyan = nekosapi.Neko()
json_search = nyan.search_image(**search_kw)
print(json_search)

"""
Return:
{'images': [{'nsfw': False, 'tags': ['1 girl', 'animal ears', 'arm behind head', 'arm up', 'ass', 'azur lane', 'bangs', 'black hair', 'blunt bangs', 'blush', 'breasts', 'cat ears', 'cat tail', 'eyebrows', 'eyebrows visible through hair', 'fang', 'from below', 'hikimayu', 'looking at viewer', 'medium breasts', 'ocean', 'one-piece swimsuit', 'red eyes', 'school swimsuit', 'short hair', 'sky', 'solo', 'stretch', 'summer', 'swimsuit', 'tail', 'thick eyebrows', 'thighhighs', 'white legwear', 'yamashiro (azur lane)'], 'likes': 13, 'favorites': 9, 'id': 'SJv4lnRhf', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'sumi (kjtd2458)', 'comments': [], 'createdAt': '2018-04-26T01:49:35.650Z', 'url': 'https://nekos.moe/image/SJv4lnRhf', 'thumbnail': 'https://nekos.moe/thumbnail/SJv4lnRhf'}, {'nsfw': False, 'tags': [':o', '1 girl', 'animal ears', 'artist name', 'ass', 'bangs', 'bikini', 'black bikini', 'black gloves', 'black legwear', 'blush', 'detached sleeves', 'eyebrows visible through hair', 'fang', 'final fantasy', 'final fantasy xiv', 'flying sweatdrops', 'from side', 'gloves', 'grey hair', 'long hair', 'looking at viewer', 'looking back', "miqo'te", 'open mouth', 'paw background', 'purple eyes', 'signature', 'simple background', 'smile', 'solo', 'swimsuit', 'tail', 'thighhighs', 'thighs', 'whisker markings', 'yellow background'], 'likes': 12, 'favorites': 7, 'id': 'Hkqh3amTM', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'sakura chiyo (konachi000)', 'comments': [], 'createdAt': '2018-04-29T22:52:33.960Z', 'url': 'https://nekos.moe/image/Hkqh3amTM', 'thumbnail': 'https://nekos.moe/thumbnail/Hkqh3amTM'}, {'nsfw': False, 'tags': [':o', '2 girls', 'animal ears', 'bangs', 'bikini', 'black bikini', 'blue eyes', 'blue hair', 'blush', 'breasts', 'cat ears', 'cat tail', 'cleavage', 'collar', 'collarbone', 'day', 'eyebrows visible through hair', 'flower', 'frilled bikini', 'frills', 'front tie top', 'hair flower', 'hair ornament', 'large breasts', 'looking at viewer', 'multiple girls', 'navel', 'ocean', 'open mouth', 'outdoors', 'paw pose', 'pink eyes', 'pink hair', 'ram (re:zero)', 're:zero kara hajimeru isekai seikatsu', 'rem (re:zero)', 'ribbon trim', 'ribbon trimmed clothes', 'short hair', 'siblings', 'side tie bikini', 'sisters', 'string bikini', 'sunlight', 'swimsuit', 'tail', 'tassel', 'twins', 'x hair ornament'], 'likes': 12, 'favorites': 6, 'id': 'r1sp9yjof', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'shouu-kun', 'comments': [], 'createdAt': '2018-04-11T01:54:11.250Z', 'url': 'https://nekos.moe/image/r1sp9yjof', 'thumbnail': 'https://nekos.moe/thumbnail/r1sp9yjof'}, {'id': 'Sk07gj3Eb', 'uploader': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'kimura (ykimu)', 'tags': ['1girl', 'animal', 'animal ears', 'black hair', 'brown eyes', 'cat', 'cat ears', 'cat tail', 'jacket', 'multicolored hair', 'multiple tails', 'nekomata', 'open clothes', 'open jacket', 'original', 'short hair', 'shorts', 'sitting', 'slit pupils', 'solo', 'tail', 'two tone hair'], 'comments': [], 'favorites': 4, 'likes': 10, 'nsfw': False, 'createdAt': '2017-07-07T05:46:13.960Z', 'url': 'https://nekos.moe/image/Sk07gj3Eb', 'thumbnail': 'https://nekos.moe/thumbnail/Sk07gj3Eb'}, {'id': 'rJ4m09sPG', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'ikomochi', 'comments': [], 'favorites': 5, 'likes': 8, 'tags': ['1 girl', ':d', 'animal ears', 'bangs', 'bell', 'black hair', 'blunt bangs', 'breasts', 'cat ears', 'cat tail', 'cleavage', 'eyebrows visible through hair', 'fang', 'fox mask', 'full body', 'grey background', 'jingle bell', 'large breasts', 'leaning forward', 'mask', 'mask on head', 'name tag', 'open mouth', 'red eyes', 'school swimsuit', 'seiza', 'short hair', 'simple background', 'sitting', 'smile', 'solo', 'sparkle', 'swimsuit', 'tail', 'tail bell', 'thighhighs', 'white legwear', 'azur lane', 'yamashiro (azur lane)'], 'nsfw': False, 'createdAt': '2018-02-22T01:34:22.735Z', 'url': 'https://nekos.moe/image/rJ4m09sPG', 'thumbnail': 'https://nekos.moe/thumbnail/rJ4m09sPG'}, {'id': 'H18kIgp5b', 'uploader': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'gomano rio', 'tags': ['1girl', ':3', 'ahoge', 'angora rabbit', 'animal', 'animal ears', 'animal on chest', 'bangs', 'black gloves', 'black hair', 'black legwear', 'black serafuku', 'blue eyes', 'blush', 'braid', 'bunny', 'cat ears', 'cat tail', 'closed mouth', 'fingerless gloves', 'full body', 'gloves', 'hair between eyes', 'hair flaps', 'hair ornament', 'hair over shoulder', 'kantai collection', 'kemonomimi mode', 'kneehighs', 'knees up', 'looking at viewer', 'lying', 'miniskirt', 'neckerchief', 'on back', 'pleated skirt', 'red neckerchief', 'remodel (kantai collection)', 'school uniform', 'serafuku', 'shigure (kantai collection)', 'short sleeves', 'single braid', 'skirt', 'tail'], 'comments': [], 'favorites': 5, 'likes': 8, 'nsfw': False, 'createdAt': '2017-09-18T07:29:34.366Z', 'url': 'https://nekos.moe/image/H18kIgp5b', 'thumbnail': 'https://nekos.moe/thumbnail/H18kIgp5b'}, {'nsfw': False, 'tags': ['1 girl', 'animal ears', 'bed', 'black hair', 'black skirt', 'blush', 'breasts', 'brown eyes', 'curtains', 'fox ears', 'fox tail', 'indoors', 'kemono friends', 'long hair', 'looking at viewer', 'lying', 'medium breasts', 'miniskirt', 'no bra', 'on bed', 'open clothes', 'open shirt', 'pillow', 'shirt', 'short sleeves', 'silver fox (kemono friends)', 'silver hair', 'skirt', 'solo', 'tail', 'window'], 'likes': 7, 'favorites': 5, 'id': 'SJ7xB3m6M', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'akashio (loli ace)', 'comments': [], 'createdAt': '2018-04-29T21:11:07.120Z', 'url': 'https://nekos.moe/image/SJ7xB3m6M', 'thumbnail': 'https://nekos.moe/thumbnail/SJ7xB3m6M'}, {'nsfw': False, 'tags': ['1 girl', 'animal ears', 'black hair', 'black legwear', 'black neckwear', 'blue eyes', 'blush', 'breasts', 'fur collar', 'gloves', 'grey wolf (kemono friends)', 'heterochromia', 'holding', 'holding pencil', 'kemono friends', 'long hair', 'long sleeves', 'looking at viewer', 'medium breasts', 'miniskirt', 'multicolored hair', 'necktie', 'pencil', 'plaid', 'plaid neckwear', 'plaid skirt', 'simple background', 'sitting', 'skirt', 'smile', 'solo', 'tail', 'thighhighs', 'two-tone hair', 'white background', 'white gloves', 'white hair', 'wolf ears', 'wolf tail', 'yellow eyes', 'zettai ryouiki'], 'likes': 7, 'favorites': 8, 'id': 'HysA4276z', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'akashio (loli ace)', 'comments': [], 'createdAt': '2018-04-29T21:10:43.289Z', 'url': 'https://nekos.moe/image/HysA4276z', 'thumbnail': 'https://nekos.moe/thumbnail/HysA4276z'}, {'nsfw': False, 'tags': [':3', '> <', '1 girl', 'animal', 'animal ears', 'aqua bikini', 'bikini', 'black cat', 'blush', 'bow', 'breasts', 'brown eyes', 'cat', 'cat ears', 'cat tail', 'closed eyes', 'closed mouth', 'collarbone', 'erune', 'frilled bikini', 'frills', 'granblue fantasy', 'grey hair', 'hair between eyes', 'hair bow', 'head tilt', 'jacket', 'long hair', 'long sleeves', 'looking at viewer', 'low ponytail', 'medium breasts', 'navel', 'open clothes', 'open jacket', 'paws', 'sen (granblue fantasy)', 'short hair', 'silver hair', 'simple background', 'small breasts', 'smile', 'solo', 'swimsuit', 'tail', 'thigh strap', 'underboob', 'whiskers', 'white background', 'yellow bow', 'yellow jacket'], 'likes': 7, 'favorites': 3, 'id': 'r1r5dQ-TG', 'uploader': {'id': 'BkCBy21se', 'username': 'brussell'}, 'approver': {'id': 'BkCBy21se', 'username': 'brussell'}, 'artist': 'itoichi.', 'comments': [], 'createdAt': '2018-04-27T22:47:40.970Z', 'url': 'https://nekos.moe/image/r1r5dQ-TG', 'thumbnail': 'https://nekos.moe/thumbnail/r1r5dQ-TG'}, {'id': 'B1K30WJpW', 'uploader': {'username': 'brussell', 'id': 'BkCBy21se'}, 'artist': 'niruanu (nitayam)', 'tags': ['1girl', ':<', 'animal', 'animal ears', 'animal on head', 'animal on lap', 'black cat', 'black footwear', 'black legwear', 'blue eyes', 'blue skirt', 'blush', 'border', 'cat', 'cat ears', 'cat tail', 'closed mouth', 'request', 'eyebrows visible through hair', 'grey background', 'grey border', 'hair between eyes', 'hair ornament', 'hairpin', 'hat', 'hat removed', 'headwear removed', 'hibiki (kantai collection)', 'highres', 'kantai collection', 'loafers', 'long hair', 'long sleeves', 'looking at viewer', 'on head', 'playing with own hair', 'pleated skirt', 'school uniform', 'serafuku', 'shirt', 'shoes', 'silver hair', 'simple background', 'skirt', 'solo', 'squatting', 'tail', 'tareme', 'thighhighs', 'verniy (kantai collection)', 'very long hair', 'white hat', 'white shirt', 'zettai ryouiki'], 'comments': [], 'favorites': 4, 'likes': 7, 'nsfw': False, 'createdAt': '2017-10-14T04:12:34.140Z', 'url': 'https://nekos.moe/image/B1K30WJpW', 'thumbnail': 'https://nekos.moe/thumbnail/B1K30WJpW'}]}
"""

#New:

search_img = nekosapi.Post.search(**search_kw)
print(search_img)