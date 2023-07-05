from setuptools import find_packages, setup

setup(
    name="directory_cms_client",
    version="12.3.1",
    url="https://github.com/uktrade/directory-cms-client",
    license="MIT",
    author="Department for International Trade",
    description="Python API client for Directory CMS.",
    packages=find_packages(),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        "directory_client_core>=7.2.4,<8.0.0",
    ],
    extras_require={
        "test": [
            "flake8==5.0.4",
            "freezegun==1.0.0",
            "pytest-django>=3.8.0,<=4.1.0",
            "pytest-sugar>=0.9.2,<1.0.0",
            "pytest==5.4.0",
            "pytest-codecov",
            "pytest-cov",
            "GitPython",
            "requests_mock==1.8.0",
            "setuptools>=45.2.0,<50.0.0",
            "twine",
            "wheel>=0.34.2,<1.0.0",
        ]
    },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Framework :: Django",
        "Framework :: Django :: 1.11",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
