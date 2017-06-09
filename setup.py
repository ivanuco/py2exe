from distutils.core import setup
import py2exe
import sys
import re

setup(name="Hola mundo",
      version="0.1",
      description="Ejemplo del funcionamiento de distutils",
      author="Ivan del Viejo",
      author_email="ivandelviejo@gmail.com",
      url="https://github.com/ivanuco",
      license="GPL",
      scripts=['./src/hello/hello.py'],
      console=['./src/hello/hello.py'],
      #options={"py2exe": {"bundle_files": 1}},
      #zipfile=None
    )