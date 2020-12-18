"""
File that exemplify the use of the client to get a json with informations of a user of the given ID.
"""

from PyNekos import nekosapi

nyan = nekosapi.Neko()
user = nyan.get_user('WwK11x1jv')
print(user)


"""
Return:
{'user': {'roles': [], 'uploads': 0, 'likes': [], 'favorites': [], 'likesReceived': 0, 'favoritesReceived': 0, 'id': 'WwK11x1jv', 'username': 'ChoiYun', 'createdAt': '2020-12-10T06:22:45.702Z'}}
"""