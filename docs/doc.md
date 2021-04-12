# Documentation
PyNekos allow you to use the Nekos.moe API in a pythonic - and easy - way. Furthermore, there's some functionalities that aren't avaible in the original API.

## Setup
Some functionalities of the API needs authentication, used for post images and regenerate and get token. This way, if you pretend to use this functionalities, you'll need to [sign up](https://nekos.moe/register)  for a (free) account that authorizes access to the [Nekos.moe API](https://docs.nekos.moe/).  If you pretend to use only the simple functionalities (like get images informations, user informations, search for images, etc), you don't need to pass nothing to the **Neko** class, see [usage](https://github.com/ChoiYun/PyNekos/blob/main/docs/doc.md#usage) section below.


## Usage
Import the package and initiate the Neko class:
```python
from PyNekos import nekosapi
nyan = nekosapi.Neko(token, username, password) # Credentials and token required only for some functionalities
```

The **Neko** class can receive three parameters: **token**, **username** and **password**.

The **token** parameter is used to regenerate the token and post images.

The **username** and **password** parameters are used to get the token.


## Quickstart
If you pretend to use the functionalities that need authentication, is better that you have everything in hands: *token*, *username* and *password*. So let's get the token using the **get_token()** function:
```python
from PyNekos.nekosapi import Neko
nyan = Neko(username="myuser", password="iwillnotshowyouthis")
token = nyan.get_token()
print(token)
```

After that, instance the object again with everything:
```python
from PyNekos.nekosapi import Neko
nyan = Neko(token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", username="myuser", password="iwillnotshowyouthis")
```

## Regenerate token
If you instance a object providing *token*, *username* and *password*, the **regen_token()** function will return the new token. Otherwise, if you only provide the *token*, the new token will not be returned, so you'll need to use the **get_token()** function again.
```python
from PyNekos.nekosapi import Neko
nyan = Neko(token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", username="myuser", password="iwillnotshowyouthis")
new_token = nyan.regen_token()
print(new_token)
```


## Get image informations

Using the **get_image(image_id)** function providing the ID of the image:
```python
json_image = nyan.get_image('Sy9sHFa8X')
print(json_image)
```


## Get random images
Using the **random_image(\*\*kwargs)** function:

- The **nsfw** parameter is type `bool`. Default *False* - Optional.

- The **count** parameter is type `int` and is the amount of images to return. Default *1* - Max *100* - Optional.
```python
safe_kw = {
    'nsfw': False,
    'count': 2
}
sfw_images_json = nyan.random_image(**safe_kw)
print(sfw_images_json)
```


## Search for images
Using the **search_image(\*\*kwargs)** function:

- The **image_id** parameter is type `string` and is the ID of the image. Default *None*  - Optional.

- The **nsfw** parameter is type `bool`. Default *False* - Optional.

- The **uploader** parameter is type `string` and is the name of the uploader. Default *None*  - Optional.

- The **artist** parameter is type `string` and is the name of the artist. Default *None*  - Optional.

- The **tags** parameter is type `list` and is the tags to filter. Default *None*  - Optional.

- The **sort** parameter is type `string` and is the method to sort. Avaible: *newest, likes, oldest, relevance*. Default *newest*  - Optional.

- The **posted_before** and **posted_after** parameters are type `string` and contain the date separated by **.** Default *None* - Optional - Ex: 2020.09.02 YYYY/MM/DD

- The **skip** parameter is type `int` and is the amount of posts to skip. Default *0*  - Optional.

- The **limit** parameter is type `int` and is the amount of posts to return. Default *20*  - Max *50* - Optional.
```python
search_kw = {
    'nsfw': False,
    'uploader': 'brussell',
    'tags': ['1 girl', 'animal ears'],
    'sort': 'likes',
    'posted_before': '2018.05.02',  # YYYY/MM/DD
    'limit': 10
}
json_search = nyan.search_image(**search_kw)
print(json_search)
```


## Get image link
Using the **get_link(image_id)** function providing the ID of the image:
```python
image_link = nyan.get_link('Sy9sHFa8X')
print(image_link)
```


## Get image thumbnail link
Using the **get_thumbnail(image_id)** function providing the ID of the image:
```python
thumb_link = nyan.get_thumbnail('Sy9sHFa8X')
print(thumb_link)
```


## Upload image
Using the **upload_image(\*\*kwargs)** function. The function can upload images from local path, from a url or from a danbooru post. Just need to select the correct one by the **upload_type** parameter:

- The **image** parameter is type `string`. For **danbooru**, should be the ID of the post. For **local**, should be the image_name.extension (image.jpg/jpeg/png). For **url**, should be the url for the image (needs to be public, can't be necessary authentication) - Required.

- The **upload_type** parameter is type `string` and is the type of upload. Avaible: *url, local, danbooru* - Required.

- The **tags** parameter is type `list` and is the tags of the image - Required except for **danbooru** posts.

- The **image_path** parameter is type `string` and is the path of the image. Required only for **local** posts.

- The **nsfw** parameter is type `bool`. Default *False* - Optional.

- The **artist** parameter is type `string` and is the author of the image - Optional - Don't required for **danbooru** posts.
```python
# Danbooru post
dan_kw = {
    'image': '2613483',
    'upload_type': 'danbooru',
    'nsfw': False
}
danbooru = nyan.upload_image(**dan_kw)
print(danbooru)

# Local post
local_kw = {
    'image': 'neko.jpg',
    'image_path': '/home/user/path/to/image/neko.jpg',
    'upload_type': 'local',
    'tags': ['student'],
    'nsfw': False
}
local = nyan.upload_image(**local_kw)
print(local)

# Url post
url_kw = {
    'image': 'https://ih1.redbubble.net/image.608339956.2125/flat,750x,075,f-pad,750x1000,f8f8f8.jpg',
    'upload_type': 'url',
    'tags': ['animal ear', 'test'],
    'nsfw': False
}
url = nyan.upload_image(**url_kw)
print(url)
```


## Get user informations
Using the **get_user(user_id)** function providing the ID of the user:
```python
user = nyan.get_user('WwK11x1jv')
print(user)
```


## Search for users
Using the **search_user(\*\*kwargs)** function:

- The **query** parameter is type `string` and is the name for search. Default *None* - Optional.

- The **skip** parameter is type `int` and is the amount of posts to skip. Default *0* - Optional.

- The **limit** parameter is type `int` and is the amount of users to return. Default *20* - Max *100* - Optional.
```python
search_kw = {
    'limit': 2
}
users = nyan.search_user(**search_kw)
print(users)
```


# Troubles
If you have any troubles using any function above, try see the [example files](https://github.com/ChoiYun/PyNekos/tree/main/examples) or feel free to open a [issue](https://github.com/ChoiYun/PyNekos/issues).
