# For Building our application as a package

from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT= '-e .'
def get_requirements(file_path:str)->List[str]:
    ''' 
    This function will return the list of requirements
    '''
    requirements= []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace('\n', '') for req in requirements]

    if HYPEN_E_DOT in requirements:
        requirements= requirements.remove(HYPEN_E_DOT)
    
    return requirements

#package details
setup(
name= 'MLProject',
version= '0.0.1',
author= 'Shyam',
author_email= 'shyamchatterjee2013@gmail.com',
packages= find_packages(),     #find all the packages in the app(if a folder contains __init__.py file, its a package)
install_requires= get_requirements('requirements.txt')  
)