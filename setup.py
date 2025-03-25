#!/usr/bin/env python

from distutils.core import setup

setup(name='rotatepdf',
      version='20150425',
      description='Rotate PDF easily from command line',
      author='Andre Miras',
      url='https://github.com/AndreMiras/rotatepdf',
      packages=['rotatepdf'],
      scripts=['rotatepdf/rotatepdf.py'],
      install_requires=["PyPDF2<3"],)
