"""Python setup.py for ideal_fishstick package"""
import io
import os
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("ideal_fishstick", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="ideal_fishstick",
    version=read("ideal_fishstick", "VERSION"),
    description="Awesome ideal_fishstick created by FEY1000",
    url="https://github.com/FEY1000/ideal-fishstick/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="FEY1000",
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["ideal_fishstick = ideal_fishstick.__main__:main"]
    },
    extras_require={"test": read_requirements("requirements-test.txt")},
)
