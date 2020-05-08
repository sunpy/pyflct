"""
==================================
Input/Output of dat files for FLCT
==================================

This example demonstrates the use of functions in `pyflct.utils`
to read and write arrays to binary ``dat`` files.
"""

import numpy as np

import pyflct.utils as utils

###########################################################################
# The original FLCT C code uses ``dat`` files for both input and
# output. So these functions can be used to read pre-existing ``dat`` files
# and write new files which keeps any previous calculations compatible with the
# existing implementation.

a = np.zeros((4, 4))
b = np.ones((4, 4))
c = np.arange(16).reshape((4, 4))

###########################################################################
# First, we will demonstrate writing to a ``dat`` file.

# We can write two arrays to dat file using flct.write_2_images
utils.write_2_images("two.dat", a, b)

# Three arrays can also be written to a dat file using flct.write_3_images
utils.write_3_images("three.dat", a, b, c)

###########################################################################
# We can get back these arrays by using the read functions in `pyflct.utils`
# It should be noted that these read functions can only read ``dat``
# files, the ones which were written using `pyflct.utils.write_2_images`,
# `pyflct.utils.read_3_images` and the IDL IO routines as given on the
# FLCT `website <http://cgem.ssl.berkeley.edu/cgi-bin/cgem/FLCT/dir?ci=tip&name=IDL-io-procedures>`__.

# Reading two arrays from a dat file
one, two = utils.read_2_images("two.dat")
# We verify that the arrays are the same.
assert np.allclose(one, a)
assert np.allclose(two, b)

# Reading three arrays from a dat file
one, two, three = utils.read_3_images("three.dat")
# We verify that the arrays are the same.
assert np.allclose(one, a)
assert np.allclose(two, b)
assert np.allclose(three, c)
