from distutils.core import setup
from Cython.Build import cythonize
import numpy
import os

os.environ["CC"] = "g++"
os.environ["CXX"] = "g++"

setup(ext_modules = cythonize(
           "big_sum.pyx",                 # our Cython source
           sources=["big_sum_implementation.cpp"],  # additional source file(s)
           language="c++",             # generate C++ code
           compiler="g++"
           ),
      include_dirs = [numpy.get_include()])
