from setuptools import setup, find_packages


setup(
    name='directory_cms_client',
    version='11.1.0',
    url='https://github.com/uktrade/directory-cms-client',
    license='MIT',
    author='Department for International Trade',
    description='Python API client for Directory CMS.',
    packages=find_packages(),
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    include_package_data=True,
    install_requires=[
        'directory_client_core>=6.0.0,<7.0.0',
    ],
    extras_require={
        'test': [
            'pytest==5.1.0',
            'pytest-cov==2.7.1',
            'pytest-sugar>=0.9.1,<1.0.0',
            'flake8==3.7.8',
            'requests_mock==1.6.0',
            'freezegun==0.3.12',
            'codecov==2.0.15',
            'twine>=1.11.0,<2.0.0',
            'wheel>=0.31.0,<1.0.0',
            'pytest-django>=3.2.1,<4.0.0',
            'setuptools>=38.6.0,<42.0.0',
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
