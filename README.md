# PYTHON_MODULE_TEMPLATE
> Template and instructions for uploading python code to PyPI as a module package.

Use the directory /[[PROJECT-NAME]] as a template for uploading python code to PyPI as a module that can be downloaded by others using pip and imported to other python programs.

Follow the instructions in [INSTALLATION](##INSTALLATION:) to configure and upload your PyPI package.

For further reading, see [https://packaging.python.org/tutorials/packaging-projects/](https://packaging.python.org/tutorials/packaging-projects/)

## INSTALLATION:

MAC OS & Linux:

0. (Optional) Create a github repo of [[MODULE-NAME1]].
1. Copy the python code of the module into the [[MODULE-NAME-OR-SUBMODULE-NAME]].py file. Leave \_\_init\_\_.py file empty.
2. Check GitHub and PyPI and choose a module name which is isn't already taken.
3. Rename [[MODULE-NAME1]], [[MODULE-NAME2]], [[MODULE-OR-SUBMODULE-NAME]] directories with your chosen module name.
4. Edit in the /[[MODULE-NAME1]]/README.md using the guide included in the file.
5. (Optional) Replace example_screenshot.png with an image of your python module being used, keeping the name of the image as 'example_screenshot.png'. If not, delete the image and it's reference in the README.md file.
6. Change 'yyyy' to the current year in LICENSE.
7. Update the fields in setup.py according to the file comments.
8. Open terminal, and enter:
    ```sh
    sudo apt-get update | apt-get -y install python3 python3-pip python-dev ipython ipython-notebook jupyter | python3 -m pip install setuptools wheel twine
    ```
9. In terminal, navigate using the `cd` command to [[MODULE-NAME1]]. To create distrubution files for upload using setup.py, enter into terminal: `python3 setup.py sdist bdist_wheel`
10. If necessary, create a PyPI account (https://pypi.org/).
11. Upload your package to PyPI by entering into terminal `python3 -m twine upload --repository pypi dist/*` and follow the prompts.
12. Download your module to your computer using terminal, enter: `python3 -m pip install [[MODULE-NAME]]`

## UPDATING MODULE:

1. Update the module python code in /[[MODULE-NAME]]/[[MODULE-NAME]].
2. Delete the /dist /build /...-info directories`.
3. Update the version number and required_modules (if necessary) in setup.py.
4. Update the changelog in the package's README.md (NOT in this README.md).
5. In terminal, navigate using the `cd` command to [[MODULE-NAME1]]. To regenerate updated /dist directory, run in terminal: `python3 setup.py sdist bdist_wheel`
6. (Optional) Update package git repo, make sure to include package release version in commit message.
7. Upload updated package to PyPI by entering in terminal: `python3 -m twine upload --repository pypi dist/*`
8. Update package installed on computer by entering in terminal `python3 -m pip install [[MODULE-NAME]] --upgrade`. Check that the module has been successfully update by entering `python3 -m pip show [[MODULE-NAME]]`

## USAGE EXAMPLE:

```python
from [[MODULE-NAME]] import [[MODULE-OR-SUBMODULE-NAME]]
[[MODULE-OR-SUBMODULE-NAME]].[[MODULE-METHOD]]
```
```python
import [[MODULE-NAME]].[[MODULE-OR-SUBMODULE-NAME]]
[[MODULE-NAME]].[[MODULE-OR-SUBMODULE-NAME]].[[MODULE-METHOD]]
```

## RELEASE HISTORY:
* 0.1.1 - 2020-09-02
    * FIXED: Fixed issues in README.md INSTALLATION.
* 0.1.0 - 2020-09-02
    * FIXED: Fixed issues in README.md INSTALLATION, UPDATING MODULE, and USAGE EXAMPLE sections.
* 0.0.2 - 2020-09-02
    * CHANGE: Updated README.md
    * CHANGE: Removed setup.ipynb
* 0.0.1 - 2020-09-02
    * Initial release

## META:

Nicholas Butterly – butterlyn888@gmail.com

Copyright (c) 2020 Nicholas Butterly. Distributed under the MIT license. See [LICENSE](LICENSE) for more information.

[https://github.com/butterlyn/PYTHON_MODULE_TEMPLATE](https://github.com/butterlyn/PYTHON_MODULE_TEMPLATE/)