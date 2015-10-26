#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from setuptools import setup, find_packages

setup(
    name="DjangoSEO_backendsupport",
    version='1.1git',
    packages=find_packages(exclude=["docs*", "regressiontests*"]),
    requires=['django (>=1.1)'],
    author="Pavel Savchenko (fork)",
    author_email="pavel@modlinltd.com",
    description="A framework for managing SEO metadata in Django.",
    long_description=open('README').read(),
    license="LICENSE",
    keywords="seo, django, framework",
    url="https://github.com/asfaltboy/django-seo",
    include_package_data=True,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "License :: OSI Approved :: Apache Software License",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development"
    ],
)
