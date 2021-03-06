from distutils.core import setup,Extension
from setuptools.command.develop import develop
from setuptools.command.install import install
from distutils.sysconfig import get_python_lib
import subprocess
import os
import sys

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        subprocess.check_call(['./package_build_scripts/build_library_package'])
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        print os.getcwd()
        subprocess.check_call(['./package_build_scripts/build_library_package'])
        install.run(self)

setup(
           name='ccextractor',
           version = '0.1',
           author      = "Skrill",
           description = "Testing setup script for generating the module",
           packages = ['ccextractor'],
           #package_dir = {'ccextractor':''},
           package_dir = {'ccextractor':''},
            
           package_data = {'ccextractor':['_ccextractor.so','ccextractor.py']},
        include_package_data=True,
           cmdclass={
               'develop': PostDevelopCommand,
               'install':PostInstallCommand,
               },
           )
"""

setup(
       name='ccextractor',
       version = '0.1',
       author      = "Skrill",
       description = "Testing setup script for generating the module",
       cmdclass={
           'develop': PostDevelopCommand,
           'install':PostInstallCommand,
           },
    )
"""