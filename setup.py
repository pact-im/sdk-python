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
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
