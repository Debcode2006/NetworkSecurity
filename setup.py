from setuptools import find_packages, setup
from typing import List

def get_requirements()->List[str]:
    
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            requirements = [line.strip() for line in lines if line.strip() != '-e .' and line.strip()!= '']
            
    except FileNotFoundError:
        print("requirements.txt not found")
        
    return requirements


setup(
    name= 'NetworkSecurity',
    version="0.0.1",
    author="Debanjan",
    author_email="sarkardebanjan137@gmail.com",
    packages=find_packages(),
    install_requires = get_requirements(),
    
)