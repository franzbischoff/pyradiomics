#!/usr/bin/env python

import versioneer

from setuptools import setup


with open('requirements.txt', 'r') as fp:
    requirements = list(filter(bool, (line.strip() for line in fp)))

setup(
    name='pyradiomics',

    url='http://github.com/Radiomics/pyradiomics#readme',

    author='pyradiomics community',
    author_email='pyradiomics@googlegroups.com',

    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),

    packages=['radiomics', 'radiomics.scripts'],
    zip_safe=False,
    data_files=[
      ('data', ['data/paramSchema.yaml', 'data/schemaFuncs.py'])],

    entry_points={
        'console_scripts': [
            'pyradiomics=radiomics.scripts.commandline:main',
            'pyradiomicsbatch=radiomics.scripts.commandlinebatch:main'
        ]},

    description='Radiomics features library for python',
    license='Slicer',

    install_requires=requirements
)
