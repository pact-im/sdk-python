#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

with open('README.md', 'r', encoding='utf-8') as readme:
    long_description = readme.read()

setup(
    name='pact_im',
    keywords='library,pact',
    long_description=long_description,
    long_description_content_type='text/markdown',
    version='0.2',
    description='PactIM Python API',
    author='Pact LLC',
    packages=find_packages(),
    install_requires=[
        'requests',
        'pydantic',
    ],
)
