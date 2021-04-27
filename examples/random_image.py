"""
Getting a random post
"""

from PIL import Image
from PyNekosOO import *

sfw_images  = Post.random(nsfw=False)
nsfw_images = Post.random(nsfw=True)
