"""pyramid_formencode_classic installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages



requires = [
    "pyramid",
    "pyramid_mailer",
    ]

setup(name="pyramid_sendmail",
      version="0.0.1",
      description="letting you use sendmail with pyramid",
      long_description="letting you use sendmail with pyramid",
      classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
        ],
      keywords="web pyramid",
      py_modules=['pyramid_sendmail'],
      author="Jonathan Vanasco",
      author_email="jonathan@findmeon.com",
      url="https://github.com/jvanasco/pyramid_sendmail",
      license="MIT",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      tests_require = requires,
      install_requires = requires,
      test_suite="tests",
      )

