import os,sys
from setuptools import setup
from Cython.Build import cythonize
file_name=input('file-name:')
setup(ext_modules = cythonize("{}".format(file_name)))
