#This will help to create my ML applications as a package
from setuptools import find_packages, setup
#This function will help in installing the required packages
from typing import List
#-e should not be in the list of the requirements
HYPHEN_E_DOT='-e .'
def getTheRequirements(file_path:str) ->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[i.replace("\n","") for i in requirements] #Replace the newline with blank

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements
     

setup(
    name = "ML_Project",
    description='This is ML application',
    version='0.0.1',
    author='Clinton Kuya',
    author_email='clintonmwangi17@gmail.com',
    packages=find_packages(),
    installs_requires=getTheRequirements('requirements.txt')




)

