#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pact_im import __version__

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='pact_im',
    keywords='library,pact',
    long_description=long_description,
    version=__version__,
    description='PactIM Python API',
    author='Pact LLC',
    packages=find_packages(),
    requires=[
        'requests',
        'pydantic',
    ],
)