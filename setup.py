from distutils.core import setup

# with open('./README.md') as f:
#     long_description = f.read()

long_description = """
PyNekos: a Python client for the Nekos.moe API
==============================================

``PyNekos`` provides a simple and pythonic way to use the `Nekos.moe
API <https://docs.nekos.moe/>`__.

The full documentation for ``PyNekos`` can be found
`here <https://github.com/ChoiYun/PyNekos/blob/main/docs/doc.md>`__.

Setup
-----

Some functionalities of the API needs authentication, used for post
images and regenerate and get token. This way, if you pretend to use
this functionalities, you'll need to sign up for a (free) account that
authorizes access to the Nekos.moe API. If you pretend to use only the
simple functionalities (like get images informations, user informations,
search for images, etc), you don't need to pass nothing to the Neko
class.

Installation
------------

``PyNekos`` requires Python 3.

Use ``pip`` to install the package from PyPI:

.. code:: bash

    pip install PyNekos

Usage
-----

Import the package and initiate the Neko class:

.. code:: python

    from PyNekos.nekosapi import Neko
    nyan = Neko()

If you pretend to use more advanced functionalities of the API, you'll
need the token. To get the token, you'll need your credentials:

.. code:: python

    from PyNekos.nekosapi import Neko
    nyan = Neko(username='myuser', password='iwillnotshowyouthis')
    token = nyan.get_token()
    print(token)

After that, instance the object again with all informations:

.. code:: python

    from PyNekos.nekosapi import Neko
    nyan = Neko(token="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", username="myuser", password="iwillnotshowyouthis")

Examples
--------

You can see the usage of all endpoints of the API in the `example
files <https://github.com/ChoiYun/PyNekos/tree/main/examples>`__.

Contributing
------------

Please contribute! If you want to fix a bug, suggest improvements, or
add new features to the project, just `open an
issue <https://github.com/ChoiYun/PyNekos/issues>`__ or send a pull
request.

"""

setup(
  name = 'PyNekos',
  packages = ['PyNekos'],
  version = '1.30',
  license='MIT',
  description = 'Python client for the https://nekos.moe/ API',
  long_description=long_description,
  # long_description_content_type='text/markdown',
  author = 'Pedro Huang',
  author_email = 'justhuangpedro@gmail.com',
  url = 'https://github.com/ChoiYun/PyNekos',
  download_url = 'https://github.com/ChoiYun/PyNekos/archive/v1.3.tar.gz',
  keywords = ['Nekos.moe', 'Neko', 'Nekos API'],
  install_requires=[            
          'requests',
          'beautifulsoup4',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)