"""
File that exemplify the use of the client to get a json with informations using the search to filter users.
"""

from PyNekos.nekosapi import Neko

nyan = Neko()
search_kw = {
    'limit': 2
}
users = nyan.search_user(**search_kw)
print(users)


"""
Return:
{'users': [{'id': 'BkCBy21se', 'username': 'brussell', 'createdAt': '2017-03-10T04:44:53.870Z', 'favoritesReceived': 1475, 'likesReceived': 2586, 'uploads': 637, 'roles': ['admin']}, {'id': 'rybWrj90g', 'username': 'Shumatsu', 'createdAt': '2017-04-23T22:04:41.492Z', 'favoritesReceived': 155, 'likesReceived': 282, 'uploads': 71, 'roles': []}]}
"""