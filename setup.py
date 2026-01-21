''' The setup.py is an essential file for packaging Python projects.
 It contains metadata about the project and instructions on how to install it.'''

from setuptools import setup, find_packages
from typing import List

# find_packages() automatically discovers all packages and sub-packages, i.e., folders with __init__.py files

def get_requirements() -> List[str]:
    """Read requirements.txt and return dependencies (skip editable flag)."""
    requirements: List[str] = []
    try:
        with open("requirements.txt", "r", encoding="utf-8") as file:
            for line in file:
                # Drop inline comments and trim whitespace
                cleaned = line.split("#", 1)[0].strip()
                if cleaned and cleaned != "-e .":
                    requirements.append(cleaned)
    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirements


setup(
    name="network_security_project",
    version="0.1.0",
    author="Raunaq Mittal",
    author_email="raunaqmittal2004@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements(),
)