"""Setup of the project in order to install it."""
#!/usr/bin/env python
from setuptools import setup, find_packages
import pathlib
import pkg_resources

with pathlib.Path('requirements.txt').open() as requirements_txt:
    req_packages = [
        str(requirement)
        for requirement
        in pkg_resources.parse_requirements(requirements_txt)
    ]

setup(
    name="centric",
    version="0.0.1",
    packages=find_packages(),
    install_requires=req_packages,
    package_data={'conf': ['conf/dataset.toml']},
    include_package_data=True,

)