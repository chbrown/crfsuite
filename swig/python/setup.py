#!/usr/bin/env python
import os
import subprocess
from distutils.core import setup, Extension
# os.system('swig -c++ -python -I../../include -o export_wrap.cpp ../export.i')

os.environ['CC'] = 'g++'
os.environ['CXX'] = 'g++'
os.environ['CPP'] = 'g++'
os.environ['LDSHARED'] = 'g++'

link_args = subprocess.check_output(['python-config', '--libs']).split()

setup(
    name='@PACKAGE@',
    version='@VERSION@',
    author='Naoaki Okazaki',
    description='CRFSuite Python module',
    py_modules=['crfsuite'],
    ext_modules=[Extension(
        '_crfsuite',
        sources=[
            'crfsuite.cpp',
            'export_wrap.cpp',
        ],
        extra_link_args=['-shared'] + link_args,
        libraries=['crfsuite', 'dl', 'python2.7'],
        language='c++',
    )],
)
