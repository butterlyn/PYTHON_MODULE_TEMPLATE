## DO NOT CHANGE
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

## CUSTOMISE WITH PACKAGE DETAILS. `#` entries require updating

required_modules = list([ # update list with all modules used in package
    #   'numpy>=1.11.3',
    #   'numba >=0.40.0',
    #   'scipy>=0.1.0',
    #   'scikit-learn>=0.19.1',
    #   'tables>=3.4.4',
    #   'traits>=4.6.0',
      'setuptools',	
	])

setuptools.setup(
    name="[[MODULE-NAME]]", # insert module name
    version="0.0.1", # update to latest release version
    author="Nicholas Butterly",
    author_email="butterlyn888@gmail.com",
    description="A small example package", # update with one-sentence package description
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/butterlyn/[[MODULE-NAME]]", # specify url to package in github
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires = required_modules,
    setup_requires = required_modules
)