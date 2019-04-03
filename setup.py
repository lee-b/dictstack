import os
from setuptools import setup

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "dictstack",
    version = "0.1.1",
    author = "Lee Braiden",
    author_email = "leebraid@gmail.com",
    description = "A multi-layer, stack-like dictionary.",
    license = "BSD",
    keywords = "dictionary map stack layer multi-level levels push pop hierarchical hierarchy tree overlay",
    packages=['dictstack', 'tests'],
    long_description=read('README.md'),
    tests_require=["tox"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
)
