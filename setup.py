import os
from setuptools import setup

os.environ['PIP_PROCESS_DEPENDENCY_LINKS'] = 1

setup(
    name='privateliba',
    version='1.0.0',
    packages=['privateliba'],
    install_requires=['privatelibb'],
    dependency_links=['git+https://github.com/manihamidi/privateB.git#egg=privatelibb-1.0.0'],
    url='',
    license='',
    author='Mani',
    author_email='',
    description=''
)
