import requests
import json
import os
from bs4 import BeautifulSoup


class NekoException(Exception):
    """ Base exception class for nekosapi.py. """
    pass


class CredentialsError(NekoException):
    """ Credentials error. Failed to login. """
    pass


class TokenError(NekoException):
    """ Token error. Invalid or don't passed token. """
    pass


class ImageError(NekoException):
    """ Image error. The image doesn't exist. """
    pass


class TypoError(NekoException):
    """ Type error. The type doesn't exist. """
    pass


class MissingParameters(NekoException):
    """ Missing parameters error. Required parameters don't given. """
    pass


class InvalidValue(NekoException):
    """ Invalid value error. The value given is invalid. """
    pass


class UserError(NekoException):
    """ User error. The user doesn't exist. """
    pass


class Neko:
    """
    User-level interface with the Nekos.moe API.
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

    def _verify_token(self):
        """
        Function that verifies if a token was provided.
        :return: bool
        """
        if self.token is not None:
            return True
        else:
            return False

    def get_token(self):
        """
        Function that returns the token of the user.
        :return: the token of the user
        """
        if self.username is not None and self.password is not None:
            payload = {"username": f"{self.username}", "password": f"{self.password}"}

            headers = {'content-type': 'application/json'}

            r = requests.post(f'{self.URL_BASE_API}/auth', data=json.dumps(payload), headers=headers)
            json_tk = json.loads(r.text)
            if r.status_code == 401:
                raise CredentialsError('Incorrect username or password.')
            return json_tk
        else:
            raise CredentialsError('No credentials providen.')

    def regen_token(self):
        """
        Function that regenerates the token and return the new token if credentials was provided.
        :return: the new token if credentials was provided
        """
        if self._verify_token() is True:
            print('Regenerating token...')
            headers = {"Authorization": f"{self.token}"}
            r = requests.post(f'{self.URL_BASE_API}/auth/regen', headers=headers)
            if r.status_code == 401:
                raise TokenError('Invalid token.')
            print('Token regenerated!')

            if self.username and self.password:
                return self.get_token()
        else:
            raise TokenError('No token provided.')

    def get_image(self, image_id):
        """
        Function that return a json with information about the image with the given ID.
        :param image_id: `str` - required (ID of the image)
        :return: a json with informations about the image matching the given ID.
        """
        r = requests.get(f'{self.URL_BASE_API}/images/{image_id}')  # Making the request
        if r.status_code == 404:
            raise ImageError('Image not found')
        json_img = json.loads(r.text)  # Creating the json
        json_img['image']['url'] = f'https://nekos.moe/image/{image_id}'  # Implementing the image url
        json_img['image']['thumbnail'] = f'https://nekos.moe/thumbnail/{image_id}'  # Implementing the thumbnail url
        return json_img

    def random_image(self, **kwargs):
        """
        Function that returns a json with information about random images
        :return: a json with information about the random images
        """

        nsfw = kwargs.get('nsfw')
        count = kwargs.get('count')

        if count:
            if count < 1 or count > 100:
                raise InvalidValue('The count value must be between 1 and 100')
            count = count
        else:
            count = 1
        if not nsfw or nsfw is False:
            nsfw = 'false'
        else:
            nsfw = 'true'

        payload = {"nsfw": f"{nsfw}", "count": count}
        r = requests.get(f'{self.URL_BASE_API}/random/image', params=payload)  # Making the request
        json_imgs = json.loads(r.text)  # Creating the json
        for i in range(0, len(json_imgs["images"])):
            image_id = json_imgs["images"][i]["id"]
            json_imgs["images"][i]['url'] = f'https://nekos.moe/image/{image_id}'  # Implementing the image url
            json_imgs["images"][i]['thumbnail'] = f'https://nekos.moe/thumbnail/{image_id}'  # Implementing the thumbna
            # il url
        return json_imgs

    def search_image(self, **kwargs):
        """
        Function that searches for images using specific filters.
        :return: a json with informations about the images that match the filters
        """

        image_id = kwargs.get('image_id')
        nsfw = kwargs.get('nsfw')
        uploader = kwargs.get('uploader')
        artist = kwargs.get('artist')
        tags = kwargs.get('tags')
        sort = kwargs.get('sort')
        posted_before = kwargs.get('posted_before')
        posted_after = kwargs.get('posted_after')
        skip = kwargs.get('skip')
        limit = kwargs.get('limit')

        data = {}

        if image_id:
            data["image_id"] = image_id
        if nsfw:
            data["nsfw"] = "true"
        else:
            data["nsfw"] = "false"
        if uploader:
            data["uploader"] = uploader
        if artist:
            data["artist"] = artist
        if tags:
            data["tags"] = tags
        if sort:
            data["sort"] = sort
        if posted_before:
            data["posted_before"] = posted_before
        if posted_after:
            data["posted_after"] = posted_after
        if skip:
            data["skip"] = skip
        if limit:
            if limit > 50:
                raise InvalidValue('The limit value must be at most 50')
            data["limit"] = limit

        headers = {'content-type': 'application/json'}

        r = requests.post(f'{self.URL_BASE_API}/images/search', data=json.dumps(data), headers=headers)
        json_imgs = json.loads(r.text)
        for i in range(0, len(json_imgs["images"])):
            image_id = json_imgs["images"][i]["id"]
            json_imgs["images"][i]['url'] = f'https://nekos.moe/image/{image_id}'  # Implementing the image url
            json_imgs["images"][i]['thumbnail'] = f'https://nekos.moe/thumbnail/{image_id}'  # Implementing the thumbna
            # il url
        return json_imgs

    def get_link(self, image_id):
        """
        Function that return the image link of a given ID
        :param image_id: `str` - required (ID of the image)
        :return: the link of the image of the given ID
        """
        return f'{self.URL_BASE}/image/{image_id}'

    def get_thumbnail(self, image_id):
        """
        Function that return the thumbnail link of a given ID
        :param image_id: `str` - required (ID of the image)
        :return: the link of the thumbnail of the given ID
        """
        return f'{self.URL_BASE}/thumbnail/{image_id}'

    @staticmethod
    def _send_image(filename, filepath, endpoint, data, headers):
        """
        Function that make the post request to send the image and all informations to the website
        :return: a json with information/status of the post
        """
        files = {"image": (filename, open(filepath, 'rb'), 'image/jpg', {'Expires': '0'})}
        r = requests.post(endpoint, data=data, headers=headers, files=files)
        if r.status_code == 401:
            raise TokenError('Invalid token.')
        json_img_post = json.loads(r.text)
        return json_img_post

    def upload_image(self, **kwargs):
        """
        Function that select the type of image upload and send everything to the _send_image() function for uploading
        :return: return the return of _send_image() function
        """
        if self._verify_token() is True:
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
            if not upload_type == 'danbooru':
                if not tags:
                    raise MissingParameters(f'Required parameters don\'t given: <tags>')
            if upload_type == 'local':
                if not image_path:
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

    def get_user(self, user_id):
        """
        Function that returns a json with informations about the user with given ID
        :param user_id: `str` - required
        :return: a json with informations about the user with given ID
        """
        r = requests.get(f'{self.URL_BASE_API}/user/{user_id}')
        if r.status_code == 404:
            raise UserError('No user with that id.')
        json_user = json.loads(r.content)
        return json_user

    # def search_user(self, query=None, skip=0, limit=20):
    def search_user(self, **kwargs):
        """
        Function that search for users using some filters
        :return: json with informations about searched users
        """
        query = kwargs.get('query')
        skip = kwargs.get('skip')
        limit = kwargs.get('limit')

        payload = {}

        if limit:
            if limit < 1 or limit > 100:
                raise InvalidValue('The limit value must be between 1 and 100')
            payload["limit"] = limit
        if skip:
            payload["skip"] = skip
        if query:
            payload["query"] = query

        headers = {'content-type': 'application/json'}

        r = requests.post(f'{self.URL_BASE_API}/users/search', data=json.dumps(payload), headers=headers)
        json_user = json.loads(r.content)
        return json_user
