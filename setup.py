"""
setup.py configuration script describing how to build and package this project.

This file is primarily used by the setuptools library and typically should not
be executed directly. See README.md for how to deploy, test, and run
the my_project project.
"""
from setuptools import setup, find_packages

import sys
sys.path.append('./src')

import my_project

setup(
    name="my_project",
    version=my_project.__version__,
    url="https://databricks.com",
    author="skuncheerathpoolakka@dmchosting.ca",
    description="wheel file based on my_project/src",
    packages=find_packages(where='./src'),
    package_dir={'': 'src'},
    entry_points={
        "packages": [
            "main=my_project.main:main"
        ]
    },
    install_requires=[
        # Dependencies in case the output wheel file is used as a library dependency.
        # For defining dependencies, when this package is used in Databricks, see:
        # https://docs.databricks.com/dev-tools/bundles/library-dependencies.html
        "setuptools"
    ],
)
