#!/usr/bin/env python
#-*- coding:utf-8 -*-


"""\
Checkout http://ffunenga.github.io/strjump for more information.
"""


import os.path
from setuptools import setup


here = os.path.abspath(os.path.dirname(__file__))
with open('strjump/version.py') as f:
    code = compile(f.read(), 'strjump/version.py', 'exec')
    exec(code)


setup(
    name='strjump',
    version=__version__,
    description="Generate a string comprising at least one digit representation of an index in herself.",
    long_description=__doc__,
    author="Filipe Funenga",
    author_email="fmafunenga@gmail.com",
    url="http://ffunenga.github.io/strjump",
    license='MIT',
    keywords='string index digit representation',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 5 - Production/Stable',
        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',
        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    packages=['strjump'],
    test_suite = 'tests',
)
