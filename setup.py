#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
from pact_im import __version__

setup(
    name='pact_im',
    version=__version__,
    description='PactIM Python API',
    author='Badrazhan Mikhail',
    packages=find_packages(),
    requires=[
        'requests'
    ],
)