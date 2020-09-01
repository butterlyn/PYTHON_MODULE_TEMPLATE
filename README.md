# PYTHON_MODULE_TEMPLATE
> Template and instructions for uploading python code to PyPI as a module package.

Use the directory /[[PROJECT-NAME]] as a template for uploading python code to PyPI as a module that can be downloaded by others using pip and imported to other python programs.

Follow the instructions in [INSTALLATION](##INSTALLATION:) to install jupyter, then run [setup.ipynb](setup.ipynb) using jupyter. [setup.ipynb](setup.ipynb) contains full instructions for configuring /[[PROJECT-NAME]] as required.

For further reading, see [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## INSTALLATION:
[[MAKE THIS A .ipynb file!!!]]
MAC OS & Linux:

In terminal, navigate to the folder containing the README.md using the `cd` command. Then enter the following into the terminal:
```sh
sudo apt-get update | sudo apt-get -y install python3 python3-pip python-dev ipython ipython-notebook setuptools wheel twine | sudo -H pip3 install jupyter | jupyter lab setup.ipynb
python3 setup.py sdist bdist_wheel
python3 -m twine upload --repository pypi dist/*
```
Leave \_\_init\_\_.py empty.

Update the year in README.md using your preferred text editor (e.g. code, vim)

## UPDATING MODULE:

1. make changes to the module python code in /[[MODULE-NAME]]/[[MODULE-NAME]] 

updating package:
1. make changes to code in package directory
2. delete contents of dist directory
3. update version number in setup.py
4. regenerate dist, reuploat to pyPI
5. update package on computer using
    sudo pip3 install [package_name] --upgrade

## USAGE EXAMPLE:

After INSTALL has been completed:
importing to a python file:
python3 -m pip install example-pkg-butterly
from example_pkg import testModule1
OR
import example_pkg.testModule1

testModule1.add_num()
OR
example_pkg.testModule1.add_num()

## RELEASE HISTORY:

* 0.0.1 - 2020-09-02
    * Initial release

## META:

Nicholas Butterly – butterlyn888@gmail.com

Copyright (c) 2020 Nicholas Butterly. Distributed under the MIT license. See [LICENSE](LICENSE) for more information.

[https://github.com/butterlyn/PYTHON_MODULE_TEMPLATE](https://github.com/butterlyn/PYTHON_MODULE_TEMPLATE/)