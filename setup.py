#!/usr/bin/env python3
from setuptools import find_packages, setup

setup(name='fplot',
      packages=find_packages(),
      version='0.1.0',
      description='matplotlib wrapper that manages plot mutation',
      author='github.com/GustavMH',
      install_requires=["numpy", "matplotlib"],
      license='MIT')
