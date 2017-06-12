"""Installer for the global-fixtures package."""

from setuptools import find_packages
from setuptools import setup


setup(
    name='global-fixtures',
    version='0.1',
    description='The purpose of this project is to test how to use global '
                'fixtures.',
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'License :: MIT License',
    ],
    author='karantan',
    author_email='karantan@gmail.com',
    url='http://github.com/karantan/global-fixtures',
    keywords='pytest, fixtures',
    license='MIT License',
    packages=find_packages('src', exclude=['ez_setup']),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'pytest',
    ],
)
