#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='pact_im',
    keywords='library,pact',
    long_description=long_description,
    version='0.1',
    description='PactIM Python API',
    author='Pact LLC',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
    ],
)