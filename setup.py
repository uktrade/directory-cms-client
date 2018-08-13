"""
Directory CMS client
"""
import ast
import re
from setuptools import setup, find_packages


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
    install_requires=[
        'directory_client_core>=4.0.0<5.0.0',
        ' w3lib>=1.19.0<2.0.0',
    ]
)
