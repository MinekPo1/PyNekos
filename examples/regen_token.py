"""
File that exemplify the use of the client to regen the token of the Nekos.moe API
If provided credentials, return the new token. If not, only regen the token.
!!! Warning: Usually it takes more than 30 seconds to regenerate the token. !!!
"""

from PyNekosOO import *

nyan = Neko(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', username='MyUser', password='iwillnotshowyouthis')
nyan.regen_token()
print(nyan.token)

"""
Return:
{'token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'}
"""