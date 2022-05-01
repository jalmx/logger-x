from setuptools import setup

# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/

with open("Readme.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="loggerx",
    version="0.1.0",
    description="A logger for the projects xizuth",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jalmx/logger-x",
    author="Xizuth",
    author_email="xizuth@gmail.com",
    license="MIT",
    packages=["loggerx"],
    python_requires=">=3.6",
    zip_safe=False,
)
