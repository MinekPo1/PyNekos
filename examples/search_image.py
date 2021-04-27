"""
Searching for images
"""

from PyNekosOO import *

search_kw = {
    'nsfw': False,
    'uploader': 'brussell',
    'tags': ['1 girl', 'animal ears'],
    'sort': 'likes',
    'posted_before': '2018.05.02',  # YYYY/MM/DD
    'limit': 10
}

search_img = Post.search(**search_kw)
print(search_img)