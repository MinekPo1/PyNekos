from distutils.core import setup

with open('README.md') as f:
    long_description = f.read()

setup(
  name = 'PyNekos',
  packages = ['PyNekos'],
  version = '0.2',
  license='MIT',
  description = 'Python client for the https://nekos.moe/ API',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Pedro Huang',
  author_email = 'justhuangpedro@gmail.com',
  url = 'https://github.com/ChoiYun/PyNekos',
  download_url = '#',
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
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.1',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
)