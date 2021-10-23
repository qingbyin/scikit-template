# -*- coding: utf-8 -*-

from __future__ import print_function

import sys

try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

from setuptools import find_packages

setup(
    name="project_name",
    version="0.0.1",
    description="",
    author="Qing Yin",
    # tell setuptools to look for any packages under 'src'
    packages=find_packages(where='src'),
    # tell setuptools that all packages will be under the 'src' directory and nowhere else
    package_dir={"": "src"},
    cmake_install_dir="src/project_name",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
)
