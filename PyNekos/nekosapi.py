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


class TypeError(NekoException):
    """ Type error. The type doesn't exist. """
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

            if self.username is not None and self.password is not None:
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

    def random_image(self, nsfw=False, count=1):
        """
        Function that returns a json with information about random images
        :param nsfw: `bool` - optinal (True/False - used to filter the result) - Default False
        :param count: `int` - optional - Default 1 (1-100 - amount of images)
        :return: a json with information about the random images
        """

        if nsfw is True:
            new_nsfw = 'true'
        else:
            new_nsfw = 'false'

        payload = {"nsfw": f"{new_nsfw}", "count": count}
        r = requests.get(f'{self.URL_BASE_API}/random/image', params=payload)  # Making the request
        json_img = json.loads(r.text)  # Creating the json
        image_id = json_img["images"][0]["id"]  # Getting the image ID
        json_img['images'][0]['url'] = f'https://nekos.moe/image/{image_id}'  # Implementing the image url
        json_img['images'][0]['thumbnail'] = f'https://nekos.moe/thumbnail/{image_id}'  # Implementing the thumbnail url
        return json_img

    def search_image(self, image_id=None, nsfw=False, uploader=None, artist=None, tags=None, sort="newest",
                     posted_before=None, posted_after=None, skip=0, limit=20):
        """
        Function that searches for images using specific filters.
        :param image_id: `str` - optional (ID of the image)
        :param nsfw: `bool` - optional (True/False - used to filter the results)
        :param uploader: `str`  - optional (Filter results of a specific uploader)
        :param artist: `str` - optional (Filter results of a specific artist)
        :param tags: `list` - optional (Filter results by tags)
        :param sort: `str` - optional - default `newest` - (newest, likes, oldest, relevance)
        :param posted_before: `str` - optional (Separated by .  or : or -) Ex: 2020.09.02 YYYY/MM/DD
        :param posted_after: `str` - optional (Separated by .  or : or -) Ex: 2020.09.02 YYYY/MM/DD
        :param skip: `int` - optional - default `0` (Number of images to skip)
        :param limit: `int` - optional - default `20` - max `50` (Ammount of images)
        :return: a json with informations about the images that match the filters above
        """

        data = {"skip": skip, "limit": limit, "sort": sort}

        if image_id is not None:
            data["image_id"] = image_id
        if nsfw is True:
            data["nsfw"] = "true"
        if nsfw is False:
            data["nsfw"] = "false"
        if uploader is not None:
            data["uploader"] = uploader
        if artist is not None:
            data["artist"] = artist
        if tags is not None:
            data["tags"] = tags
        if posted_before is not None:
            data["posted_before"] = posted_before
        if posted_after is not None:
            data["posted_after"] = posted_after

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

    def _send_image(self, filename, filepath, endpoint, data, headers):
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

    def upload_image(self, image, upload_type, tags=None, image_path=None, nsfw=False, artist=None):
        """
        Function that select the type of image upload and send everything to the _send_image() function for uploading
        :param image: `str` - required (name.extension/image link/Danbooru post ID)
        :param upload_type: `str` - required (url/local/danbooru)
        :param tags: `list` - required - except for danbooru posts - (Tags to be used)
        :param image_path: `str` - optional - except for local posts (Path of the image)
        :param nsfw: `bool` - optional (True/False) - Default False
        :param artist: `str` - optional
        :return: return the return of _send_image() function
        """
        if self._verify_token() is True:
            endpoint = f"{self.URL_BASE_API}/images"
            data = {"tags": tags}

            if artist is not None:
                data["artist"] = artist
            if nsfw is True:
                data["nsfw"] = "true"

            headers = {"Authorization": f'{self.token}'}

            if upload_type == 'url':
                img = requests.get(image)

                with open('image.jpg', 'wb') as f:
                    f.write(img.content)

                filename = 'image.jpg'
                filepath = f'{os.getcwd()}/image.jpg'

                a = self._send_image(filename, filepath, endpoint, data, headers)
                os.remove('image.jpg')
                return a
            elif upload_type == 'local':
                return self._send_image(image, image_path, endpoint, data, headers)
            elif upload_type == 'danbooru':
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
                raise TypeError('Type unrecognized.')
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

    def search_user(self, query=None, skip=0, limit=20):
        """
        Function that search for users using some filters
        :param query: `str` - optional - default: None
        :param skip: `str` - optional - default: 0
        :param limit: `str` - optional - default: 20
        :return: json with informations about searched users
        """
        payload = {"limit": limit, "skip": skip}

        if query is not None:
            payload["query"] = query

        headers = {'content-type': 'application/json'}

        r = requests.post(f'{self.URL_BASE_API}/users/search', data=json.dumps(payload), headers=headers)
        json_user = json.loads(r.content)
        return json_user
