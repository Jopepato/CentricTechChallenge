"""Setup of the project in order to install it."""
#!/usr/bin/env python
from setuptools import setup, find_packages
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    install_requires = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="centric",
    version="0.0.1",
    packages=find_packages(),
    install_requires=install_requires,
)