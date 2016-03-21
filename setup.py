"""
This module defines the attributes of the
PyPI package for the mbed SDK test suite ecosystem tools
"""

import os
from distutils.core import setup
from setuptools import find_packages

DESCRIPTION = "Tool to generates TOC for git markdown"
OWNER_NAMES = 'Przemyslaw Wirkus'
OWNER_EMAILS = 'Przemyslaw.Wirkus@arm.com'


# Utility function to cat in a file (used for the README)
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='git-toc',
      version='0.1.2',
      description=DESCRIPTION,
      long_description=read('README.md'),
      author=OWNER_NAMES,
      author_email=OWNER_EMAILS,
      maintainer=OWNER_NAMES,
      maintainer_email=OWNER_EMAILS,
      url='https://github.com/PrzemekWirkus/git-toc',
      packages=find_packages(),
      license="Apache-2.0",
      test_suite = 'test',
      entry_points={
        "console_scripts": [
            "gittoc=gittoc:main",
        ],
      },
      install_requires=[]
    )
