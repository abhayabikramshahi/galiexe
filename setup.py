# setup.py

from setuptools import setup, find_packages

setup(
    name='mymodule',
    version='0.1.0',
    packages=find_packages(),
    description='A simple custom Python module built by Abhaya',
    author='Abhaya',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/mymodule',  # if public
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
