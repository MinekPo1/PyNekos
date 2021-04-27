from io import BytesIO
from typing import Any, BinaryIO, Literal, Optional, overload
import requests
import json

class CredentialsError(Exception):
    """ Credentials error. Failed to login or unauthorised. """
    pass

class User:
    """
    Object represending a user account on nekos.moe.
    TODO: Extend doc string.
    """
    roles:list[str]
    uploads:int
    likes:list[str]
    favorites:list[str]
    likesReceived:int
    favoritesReceived:int
    id:str
    username:str
    createdAt:str

    def __init__(self,id:str,update = True) -> None:
        self.id = id
        if update:self.update()
    def update(self):
        r = requests.get('https://nekos.moe/api/v1/user/'+self.id)
        self._data = r.json()
    def __getattr__(self, name: str) -> Any:
        if name in self._data:
            return self._data[name]
        else:
            super().__getattribute__(name)
    def __repr__(self):
        return(f"<nekos.moe user {self.id}>")

    @classmethod
    def _from_json(cls,json: dict):
        out = cls(json['id'],False)
        out._data = json
        return out

    @classmethod
    def search(cls,*,query: str = "",skip:int = 0,limit:int = 20) -> list:
        r = requests.post("https://nekos.moe/api/v1/users/search",json = {"query":query,"skip":skip,"limit":limit})
        users = r.json()['users']
        return [cls._from_json(user) for user in users]

class Post:
    """
    Object representing a post on nekos.moe.
    TODO: Extend doc string.
    """
    tags: list[str]
    nsfw: bool
    id: str
    uploader: User
    pending:bool
    likes: Optional[int]
    favorites: Optional[int]
    aprover: Optional[User]

    def __init__(self,id,update = True):
        self.id = id
        self._data: Optional[dict] = None
        if update:
            self.update()
    def update(self):
        r = requests.get('https://nekos.moe/api/v1/images/self.id')
        self._data = r.json()
        self._data['uploader'] = User(self._data['uploader']['id'])
        if 'aprover' in self._data: # type:ignore
            self._data['aprover'] = User(self._data['aprover']['id'])
    def get_image(self) -> BytesIO:
        r = requests.get('https://nekos.moe/image/'+self.id)
        return BytesIO(r.content)
    def get_thumbnail(self) -> BytesIO:
        r = requests.get('https://nekos.moe/thumbnail/'+self.id)
        return BytesIO(r.content)
    def __getattr__(self, name: str) -> Any:
        if self._data != None and name in self._data:
            return self._data[name]
        else:
            super().__getattribute__(name)
    def __repr__(self):
        return(f"<nekos.moe image {self.id}>")

    @classmethod
    def _from_json(cls,json: dict):
        out = cls(json['id'],False)
        out._data = json
        out._data['uploader'] = User(out._data['uploader']['id'])
        if 'aprover' in out._data: # type:ignore
            out._data['aprover'] = User(out._data['aprover']['id'])
        return out

    @overload
    @classmethod
    def search(cls,*, id:int = None, nsfw: bool = None, uploader:str = None, artist:str = None,
        tags:list[str] = None, sort:Literal['newest','likes','oldest','relevance'] = None,posted_before:int = None,
        posted_after:int = None, skip:int = None, limit:int = None) -> list:...
    @overload
    @classmethod
    def search(cls) -> list:...
    @classmethod
    def search(cls,**kwargs):
        r = requests.post("https://nekos.moe/api/v1/images/search",)
        posts = r.json()['images']
        out = [cls._from_json(post) for post in posts]
        return out

    @classmethod
    def random(cls,*,nsfw: bool = None,count: int = 1):
        r = requests.get("https://nekos.moe/api/v1/random/image",data = {'nsfw':str(nsfw).lower,'count':count})
        return [cls._from_json(image) for image in r.json()['images']]

class Neko:
    """
    Object representing a nekos.moe client
    Args: token (`str`, optional): token provided by Nekos.moe - Used to upload images.
    Args: username (`str`, optional): username used to log in in the Nekos.moe website - Used to get token.
    Args: password (`str`, optional): password used to log in in the Nekos.moe website - Used to get token.
    """
    def __init__(self, token=None, username=None, password=None):
        self.token = token
        self.username = username
        self.password = password
        self.URL_BASE_API = 'https://nekos.moe/api/v1'
        self.URL_BASE = 'https://nekos.moe'

    def get_token(self) -> None:
        """
        Method to retrieve token using username and password.
        """
        if self.username != None and self.password != None:
            payload = {"username": f"{self.username}", "password": f"{self.password}"}

            headers = {'content-type': 'application/json'}

            r = requests.post(f'{self.URL_BASE_API}/auth', data=json.dumps(payload), headers=headers)
            json_tk = json.loads(r.text)
            if r.status_code == 401:
                raise CredentialsError('Incorrect username or password.')
            self.token = json_tk['token']
        else:
            raise CredentialsError('No credentials provided.')

    def regen_token(self,get_token = True) -> None:
        """
        Function that regenerates the token and return the new token if credentials was provided.
        :return: the new token if credentials was provided
        """
        if self.token != None:
            print('Regenerating token...')
            headers = {"Authorization": f"{self.token}"}
            r = requests.post(f'{self.URL_BASE_API}/auth/regen', headers=headers)
            if r.status_code == 401:
                raise CredentialsError('Invalid token.')
            if not(get_token): return
            if self.username and self.password:
                self.token = self.get_token()
            else: raise CredentialsError("username and password are reqired to get token")
        else:
            raise CredentialsError('No token provided.')

    @overload
    def upload_image(self, *, type:Literal["file"], path:str, author:str = "random anon", nsfw:bool = False,
        tags:list[str] = None): ...
    @overload
    def upload_image(self, *, type:Literal["stream"], stream:BinaryIO, author:str = "random anon", nsfw:bool = False,
        tags:list[str] = None): ...
    @overload
    def upload_image(self, *, type:Literal["link"], link:str, author:str = "random anon", nsfw:bool = False,
        tags:list[str] = None): ...
    @overload
    def upload_image(self, *, type:Literal["danbooru"], link:str): NotImplemented

    def upload_image(self, **kwargs):
        """
        """
        if self.token == None:
            raise ValueError("Token not provided.")

        #check type and get file like object
        if 'type' not in kwargs:
            raise TypeError("upload_image() missing at least one reqired keyword-only argument: type")

        elif kwargs['type'] == "file":
            if 'path' not in kwargs:
                raise TypeError("upload_image() missing at least one reqired keyword-only argument: path")
            stream = open(kwargs['path'])

        elif kwargs['type'] == "stream":
            if 'stream' not in kwargs:
                raise TypeError("upload_image() missing at least one reqired keyword-only argument: stream")
            stream = kwargs['stream']

        elif kwargs['type'] == "link":
            if 'link' not in kwargs:
                raise TypeError("upload_image() missing at least one reqired keyword-only argument: link")
            r = requests.get(kwargs['link'])
            stream = BytesIO(r.content)

        elif kwargs['type'] == "danbooru":
            raise NotImplementedError("danbooru uploading is not yet implemented.")
        else:
            raise ValueError("Unknown type.")

        data = {
            'nsfw':False,
            'tags':[],
            'artist':None,
        }

        for key in data:
            if key in kwargs:data[key] = kwargs[key]
        data['file'] = stream.read()

        req = requests.post("https://nekos.moe/api/v1/images",json=data)
        if req.status_code == 200:
            return Post._from_json(req.json()['image'])
        if req.status_code == 409:
            raise ValueError("Image already uploaded")
        if req.status_code == 403:
            raise CredentialsError("Only verified accounts can upload images.")
        req.raise_for_status()
        #old code
        #TODO: remove it
        """
        if self.token != None:
            image = kwargs.get('image')
            upload_type = kwargs.get('upload_type')
            tags = kwargs.get('tags')
            image_path = kwargs.get('image_path')
            nsfw = kwargs.get('nsfw')
            artist = kwargs.get('artist')

            if not image:
                raise MissingParameters(f'Required parameters don\'t given: <image>')
            if not upload_type:
                raise MissingParameters(f'Required parameters don\'t given: <upload_type>')
            if upload_type != 'danbooru' and tags == None:
                raise MissingParameters(f'Required parameters don\'t given: <tags>')
            if upload_type == 'local' and image_path == None:
                raise MissingParameters(f'Required parameters don\'t given: <image_path>')
            endpoint = f"{self.URL_BASE_API}/images"
            data = {}

            if artist:
                data["artist"] = artist
            if nsfw is True:
                data["nsfw"] = 'true'
            if not nsfw:
                data["nsfw"] = 'false'
            if tags:
                data["tags"] = tags

            headers = {"Authorization": f'{self.token}'}

            # Upload image by URL
            if upload_type == 'url':
                img = requests.get(image)

                with open('image.jpg', 'wb') as f:
                    f.write(img.content)

                filename = 'image.jpg'
                filepath = f'{os.getcwd()}/image.jpg'

                a = self._send_image(filename, filepath, endpoint, data, headers)
                os.remove('image.jpg')
                return a
            elif upload_type == 'local':  # Local upload
                return self._send_image(image, image_path, endpoint, data, headers)
            elif upload_type == 'danbooru':  # Danbooru upload
                r = requests.get(f'https://danbooru.donmai.us/posts/{image}')
                soup = BeautifulSoup(r.content, 'html.parser')
                artist = soup.find('li', {'class': 'tag-type-1'}).get('data-tag-name')
                class_tags = soup.findAll('li', {'class': 'tag-type-0'})
                image_url = soup.find('img', {'id': 'image'}).get('src')
                img_tags = []
                for i in class_tags:
                    img_tags.append(i.get('data-tag-name'))

                img = requests.get(image_url)

                with open('image.jpg', 'wb') as f:
                    f.write(img.content)

                filename = 'image.jpg'
                filepath = f'{os.getcwd()}/image.jpg'

                data["artist"] = artist
                data["tags"] = img_tags

                a = self._send_image(filename, filepath, endpoint, data, headers)
                os.remove('image.jpg')
                return a
            else:
                raise TypoError('Type unrecognized.')
        else:
            raise TokenError('No token provided.')
        """

    def add_favorite(self,post: Post):
        requests.patch(f"https://nekos.moe/api/v1/image/{post.id}/relationship",headers={
                "Authorization":self.token,
            },
            json = {
                "type":"favorite",
                "create":True
            }
        )
    def remove_favorite(self,post: Post):
        requests.patch(f"https://nekos.moe/api/v1/image/{post.id}/relationship",headers={
                "Authorization":self.token,
            },
            json = {
                "type":"favorite",
                "create":False
            }
        )
    def add_like(self,post: Post):
        requests.patch(f"https://nekos.moe/api/v1/image/{post.id}/relationship",headers={
                "Authorization":self.token,
            },
            json = {
                "type":"like",
                "create":True
            }
        )
    def remove_like(self,post: Post):
        requests.patch(f"https://nekos.moe/api/v1/image/{post.id}/relationship",headers={
                "Authorization":self.token,
            },
            json = {
                "type":"like",
                "create":False
            }
        )
