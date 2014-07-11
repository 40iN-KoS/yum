# -*- coding: utf-8 -*-
import yum

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='yum',
    version=yum.__version__,
    description='Simple objects',
    long_description=readme,
    author='Konstantin Sorokin',
    author_email='mr40@ya.ru',
    classifiers=(
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
    ),
)
