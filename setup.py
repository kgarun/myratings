#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
	'requests>=2.18.4',
	'bs4',
]

setup_requirements = [
    # TODO(kgarun): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='myratings',
    version='1.0.0',
    description="Displays ratings of the user from various competitive programming sites in the terminal !!",
    long_description=readme + '\n\n' + history,
    author="Arun KG",
    author_email='kgarun50@gmail.com',
    url='https://github.com/kgarun/myratings',
    packages=['myratings',],
    entry_points={
        'console_scripts': [
            'myratings=myratings.myratings:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='myratings',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
		'Topic :: Terminals',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.5',	
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
