from setuptools import setup, find_packages
import subprocess

from pip._internal import main as pipmain
import sys
import warnings
import os

cmdclass = {}
ext_modules = []

setup(
    name='apex',
    version='0.1',
    packages=find_packages(exclude=('build',
                                    'csrc',
                                    'include',
                                    'tests',
                                    'dist',
                                    'docs',
                                    'tests',
                                    'examples',
                                    'apex.egg-info',)),
    description='PyTorch Extensions written by NVIDIA',
    ext_modules=ext_modules,
    cmdclass=cmdclass,
)
