#!/usr/bin/python

from setuptools import setup, find_packages

setup(
    name='pygments-custom',
    description='Extending the Pygments lexer with custom keywords.',
    long_description=open('README.md').read(),
    keywords='pygments lexer keyword typedef',

    packages=find_packages(),
    install_requires=['pygments >= 1.4'],

    entry_points='''[pygments.lexers]
                    custom=pygments_custom:CustomLexer''',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Plugins',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
