from setuptools import find_packages, setup
from typing import List

def get_requirements() -> List[str]:
    """
    Reads requirements.txt and returns a list of dependencies
    """
    with open("requirements.txt", "r") as f:
        requirement_list = f.read().splitlines()

    # Remove "-e ." if present (since setuptools handles it)
    requirement_list = [req for req in requirement_list if req != "-e ."]
    
    return requirement_list

setup(
    name="flipkart",
    version="0.0.1",
    author="Gaurav-yadav",
    author_email="gauravscriptx@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)
