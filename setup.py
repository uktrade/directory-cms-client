from setuptools import setup, find_packages


setup(
    name='directory_cms_client',
    version='11.1.1',
    url='https://github.com/uktrade/directory-cms-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Directory CMS.',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'directory_client_core>=6.1.0,<7.0.0',
    ],
    extras_require={
        'test': [
            'codecov==2.0.15',
            'flake8==3.7.9',
            'freezegun==0.3.15',
            'pytest-cov==2.8.1',
            'pytest-django>=3.8.0,<4.0.0',
            'pytest-sugar>=0.9.2,<1.0.0',
            'pytest==5.3.5',
            'requests_mock==1.7.0',
            'setuptools>=45.2.0,<50.0.0',
            'twine>=3.1.1,<4.0.0',
            'wheel>=0.34.2,<1.0.0',
        ]
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
