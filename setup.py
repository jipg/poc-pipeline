"""setup.py file."""
from setuptools import find_packages, setup

from src import __version__

setup(
    author="Jorge Posada",
    author_email="jorge.posada@biogen.com",
    python_requires=">=3.8",
    install_requires="requirements",
    include_package_data=True,
    keywords="src",
    name="src",
    packages=find_packages(include=["src", "src.*"]),
    version=__version__,
)
