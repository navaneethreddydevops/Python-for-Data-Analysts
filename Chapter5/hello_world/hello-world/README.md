```
setup.py
```
```
from setuptools import setup, find_packages

setup(
    name="hello-world",
    version="0.0.1",
    author="Navaneeth Reddy",
    author_email="navaneethreddydevops@gmail.com",
    url="http://navaneethreddydevops.com",
    description="A hello world example package",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
```
```
python3 setup.py sdist
```
```
This will create a Python Package in dist/ folder as a tar.gz file
Also a egg folder with required packages requiremts.txt and package INFO
```
