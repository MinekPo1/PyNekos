"""
File that exemplify the use of the client to get the token of the Nekos.moe API
"""

from PyNekos.nekosapi import Neko

nyan = Neko(username='MyUser', password='iwillnotshowyouthis')
token = nyan.get_token()
print(token)


"""
Return:
{'token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
"""