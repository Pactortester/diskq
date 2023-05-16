#!/usr/bin/env python
from setuptools import find_packages
from setuptools import setup

from diskq import __version__

with open("README.md", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="diskq",
    version=f"{__version__}",
    keywords=[
        "diskq",
        "queue",
        "persistentqueue",
        "persist",
        "disk",
        "pqueue",
        "diskqueue",
        "tools",
    ],
    description="DiskQ is a Python package that provides persistent queues using disk storage",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache License 2.0",
    url="https://github.com/Pactortester/diskq.git",
    author="lijiawei",
    author_email="jiawei.li2@qq.com",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console :: Curses",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    platforms="any",
    install_requires=[
        "dill",
    ],
)
