"""
File that exemplify the use of the client to get a json with informations using the search to filter users.
"""

from PyNekosOO import *

search_kw = {
    'limit': 2
}

users = User.search(**search_kw)