from setuptools import setup, find_packages

import os

here = os.path.dirname(__file__)

requires = [
    "pyramid",
    "rebecca.repository",
    "setuptools>=0.7",
]

tests_require = [
    "testfixtures",
]

readme = open(os.path.join(here, "README.rst")).read()
changes = open(os.path.join(here, "CHANGES.txt")).read()


setup(
    name="rebecca.login",
    version="0.1",
    author="Atsushi Odagiri",
    author_email="aodagx@gmail.com",
    url="https://github.com/rebeccaframework/rebecca.login",
    namespace_packages=["rebecca"],
    packages=find_packages(),
    long_description=readme + "\n" + changes,
    install_requires=requires,
    tests_require=tests_require,
    extras_require={
        "testing": tests_require,
    },
    test_suite="rebecca.login",
    license="MIT",
)
