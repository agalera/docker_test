#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name="docker_test",
    version="0.0.1",
    author="Alberto Galera",
    author_email="galerajimenez@gmail.com",
    description="Test Application",
    long_description="long_description",
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",],
    install_requires=[],
)

