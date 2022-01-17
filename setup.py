from setuptools import setup, find_packages

setup(
    author='Thomas Thelen',
    description='A CLI for working with SWRL rules.',
    license="Apache License, Version 2.0",
    entry_points={
        'console_scripts': [
            'swrlcli=swrlcli.src.cli:reason'
        ]
    },
    name='swrlcli',
    version='0.1.0',
    install_requires=['click', 'owlready2'],
    packages=find_packages(exclude=("tests",)),
    python_requires='>=3.9'
)
