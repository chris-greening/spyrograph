import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="spyrograph",
    version="0.2.0",
    author="Chris Greening",
    author_email="chris@christophergreening.com",
    description="Library for drawing spirographs in Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/chris-greening/spyrograph",
    packages=[],
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
