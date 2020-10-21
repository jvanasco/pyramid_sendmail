"""pyramid_sendmail installation script.
"""
import os

from setuptools import setup
from setuptools import find_packages

HERE = os.path.abspath(os.path.dirname(__file__))
long_description = description = "Letting you use sendmail with Pyramid"
with open(os.path.join(HERE, "README.md")) as fp:
    long_description = fp.read()

requires = [
    "pyramid",
    "pyramid_mailer",
    "repoze.sendmail",
]
tests_require = ["pytest"]
testing_extras = tests_require + []

setup(
    name="pyramid_sendmail",
    version="0.0.1",
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Intended Audience :: Developers",
        "Framework :: Pyramid",
        "Programming Language :: Python",
        "License :: OSI Approved :: BSD License",
    ],
    keywords="web pyramid email sendmail",
    packages=["pyramid_sendmail"],
    author="Jonathan Vanasco",
    author_email="jonathan@findmeon.com",
    url="https://github.com/jvanasco/pyramid_sendmail",
    license="MIT",
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        "testing": testing_extras,
    },
    test_suite="tests",
)
