# Documentation

## Content

- [Quickstart](#Quickstart)

- [Post](#Post)

  - [Class methods](#Post%20lass%20methods%20)

    - [Search](#Search%20post)

    - [Random](#Random)

    - [_from_json](#_from_json)

  - [get_image](#get_image)

  - [update](#update%20post)

  - [get_tumbnail](#get_tumbnail)

  - [Read only data](#Post%20read%20only%20data)

- [User](#User)

  - [Class methods](#User%20class%20methods)

    - [Search](#Search%20users)

    - [_from_json](#User%20_from_json)

  - [update](Update%20user)

- [Neko](#Neko)

  - [Authorisation](#Authorisation)

  - [Upload image](#Upload%20image)

  - [Reaction methods](#Reaction%20Methods)

## Quickstart

The module provides three classes (+ an exception).

These are:

[`Post`](#Post) - used to interact with posts, also known as images.

[`User`](#User) - used to interact with users.

[`Neko`](#Neko) - used as a client object.

## Post

`__init__` arguments:

`id` - id of the post.

`update` - `bool`, `True` by default. If `False`, the details won't be downloaded.

### Post class methods

These are alternative ways of getting a `Post` object.

#### Search post

`search()`

Optional keyword arguments:

`id` - post id. Why would you use this? I don't know. But its here.

`nsfw` - `bool` or `None`. If its a `bool` then only nsfw or sfw post will be found. If `None` then both will be shown.

`uploader` - `str` describing the uploader.

`artist` - `str` describing the author.

`tags` - `list[str]` with the desired tags.

`sort` - either `'newest'`, `'likes'`, `'oldest'` or `'relevance'`. How the posts are ordered.

`posted_before` - `int`, the maximum amount of milliseconds from 1.01.1970 to the upload.

`posted_after` - `int`, the minimum amount of milliseconds from 1.01.1970 to the upload.

`skip` - `int` of posts to skip.

`limit` - `int`, maximum amount of posts to get.

returns: `list[Post]` containing the found posts.

#### random post

`random()`

Optional keyword arguments:

`nsfw` - `bool` or `None`. If its a `bool` then only nsfw or sfw post will be found. If `None` then both will be shown.

`count` - `int`, `1` by default, the amount of posts to fetch.

returns: `list[Post]` containing the fetched posts.

#### Post _from_json

`_from_json()`

Way of creating a `Post` instance from a dictionary. Used by the wrapper.

### update post

`update()`

Function to update the data about the post.

### get_image

`get_image()`

Returnes a file like object of the image.

### get_thumbnail

`get_thumbnail()`

Returnes a file like object containing a small version of the image.

### Post read only data

|name|type|description|
|:-:|:-:|:-:|
|tags|`list[str]`|list of tags a post has|
|nsfw|`bool`|wherever a post contains adult material|
|id|`str`|id of the post|
|uploader|`User`|the uploader of the post|
|pending|`bool`|if the post if pending or not|
|data not only available for pending posts|
|likes|`int`|number of likes|
|favorites|`int`|number of favorites|
|approver|`User`|the approver of the post|

## User

These are alternative ways of getting a `Post` object.

### User class methods

Alternative ways of creating `User` objects.

#### Search users

`search()`

Optional keyword arguments:

`query` - `str` to be found in usernames

`skip` - `int` amount to skip

`limit` - `int` maximum to find

#### User _from_json

`_from_json()`

Way of creating a `User` instance from a dictionary. Used by the wrapper.

### Update user

Function to update the data about the post.

## Neko

`__init__` arguments:

`token` - optional, token to authenticate using.

`username` - optional, used to get token using the `get_token` method

`password` - optional, used to get token using the `get_token` method

### Authorisation

If you want to use to use functionalities of the API requiring authorisation, you'll need the token. To get the token, you'll need your credentials:

```python
from PyNekosOO import *
nyan = Neko(username='myuser', password='iwillnotshowyouthis')
nyan.get_token()
```

Afterwards the `Neko` instance is authorised.

### Regenerate token

Using an authorised `Neko` instance you can regenerate the token. This will cause the exsisting token to be no longer valid.

Optionaly we can pass a boolean. If `False` is passed in the token will not be retrived.

```python
#assuming nyan is an authrised Neko instance
nyan.regen_token()
#with out getting the token:
nyan.regen_token(False)
#or
nyan.regen_token(get_token = False)
```

## Upload image

Uploads an image. Requires the `Neko` object is authenticated as a verified user.

Enter upload type using the keyword argument `type`. Must be either `"file"`, `"stream"`, `"link"` or `"danbooru"`. Will affect which arguments are required.

|argument name|value type|description|file|stream|link|danbooru|
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
|path|`str`|path of the image| required | - |
|stream|file like|stream containing the image| - | required | - |
|link|`str`|link to the image/danbooru post| - || required |
|author|`str`|artist name/nickname|optional||| - |
|tags|`list[str]`|tags|optional||| - |
|nsfw|`bool`|if the image contains adult material or not|optional||| - |

Returns the post.

## Reaction methods

These four methods allow for adding or removing a like or favorite from a post. All take a `Post` instance as an argument.

|method name|description|
|:-:|:-:|
|add_favorite|adds post to favorites|
|remove_favorite|removes post from favorites|
|add_like|adds post to liked|
|remove_like|removes post from liked|
