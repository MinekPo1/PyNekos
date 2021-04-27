# PyNekosOO: a Python wrapper for the Nekos.moe API

`PyNekosOO` provides a simple and pythonic way to use the [Nekos.moe API](https://docs.nekos.moe/). Fork of [ChoiYun's wrapper](https://github.com/ChoiYun/PyNekos) focused on allowing the user not to work with raw json data.

The full documentation for `PyNekosOO` can be found [here](https://github.com/MinekPo1/PyNekos/blob/main/docs/doc.md).

## Setup

Some functionalities of the API require authentication, for example posting images, regenerating the token adding likes and favorites. If you want to use these functionalities you have to have an account. Create one [here](https://nekos.moe/register). Note that this is optional as you can use most of the wrapper with out an account.

<!--
## Installation

`PyNekosOO` requires Python 3.8 or above.

Use `pip` to install the package from PyPI:

```bash
pip install PyNekosOO
```
-->

## Authorisation

If you want to use to use functionalities of the API requiring authorisation, you'll need the token. To get the token, you'll need your credentials:

```python
from PyNekosOO import *
nyan = Neko(username='myuser', password='iwillnotshowyouthis')
nyan.get_token()
```

Afterwards the `Neko` instance is authorised.

## Examples

You can see the usage of all endpoints of the API in the [example files](https://github.com/MinekPo1/PyNekos/tree/main/examples).

## Contributing

Please contribute! If you want to fix a bug, suggest improvements, or add new features to the project, just [open an issue](https://github.com/MinekPo1/PyNekos/issues) or fork the project.
