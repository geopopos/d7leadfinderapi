import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="d7-lead-finder-api-geopopos",
    version="0.0.1",
    author="Georgios Roros",
    author_email="george.roros25@gmail.com",
    description="A pythonic api wrapper for the D7 Lead Finder API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/geopopos/d7leadfinderapi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)