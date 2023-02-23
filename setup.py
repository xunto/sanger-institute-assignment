from distutils.core import setup

from setuptools import find_packages

setup(
    name="sanger.assignment",
    version="1.0",
    author="Valentin Orlov",
    author_email="v.orlov@gmail.com",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=[
        "click==8.*",
        "fastq==2.*",
    ],
)
