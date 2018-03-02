"""
Export Directory API client
"""
import ast
import re
from setuptools import setup, find_packages

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip


pfile = Project(chdir=False).parsed_pipfile


def get_version():
    pattern = re.compile(r'__version__\s+=\s+(.*)')

    with open('directory_cms_client/version.py', 'rb') as src:
        return str(ast.literal_eval(
            pattern.search(src.read().decode('utf-8')).group(1)
        ))


setup(
    name='directory_cms_client',
    version=get_version(),
    url='https://github.com/uktrade/directory-cms-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Directory CMS.',
    packages=find_packages(),
    long_description=open('README.md').read(),
    include_package_data=True,
    install_requires=convert_deps_to_pip(pfile['packages'], r=False),
)
