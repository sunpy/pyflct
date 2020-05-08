****************************************************************
pyflct: A Python wrapper for Fourier Local Correlation Tracking.
****************************************************************

.. image:: http://img.shields.io/badge/powered%20by-SunPy-orange.svg?style=flat
    :target: http://www.sunpy.org
    :alt: Powered by SunPy Badge

pyflct is a Python wrapper around the `Fourier Local Correlation Tracking C library <http://cgem.ssl.berkeley.edu/cgi-bin/cgem/FLCT/home>`__.
`Our built documentation is available here <https://pyflct.readthedocs.io/en/latest/>`__.

Installing
==========

Linux and Mac OS
----------------

The simplest way to install this library is through pip::

    $ pip install pyflct

This will install the pre-compiled binary wheels for these two platforms.

Windows
-------

We only officially support Windows through Anaconda.
But we do have rough instructions in our documentation if you want to install it manually.

`Please find the instructions in our documentation <https://pyflct.readthedocs.io/en/latest/install.html>`__.

Getting Help
============

Stop by our chat room `#sunpy:matrix.org`_ if you have any questions.

Contributing
============

If you would like to get involved, check out the `Developer's Guide`_ section of the SunPy docs.
Help is always welcome so let us know what you like to work on, or check out the `issues page`_ for the list of known outstanding items.
For more information on general contributing, please read our `contributing guide`_.

If you want help develop pyflct you will need to install it from GitHub.
The best way to do this is to create a new python virtual environment (of your choice) and then fork this repository.

Then::

    $ git clone https://github.com/<username>/pyflct.git
    $ cd pyflct
    $ pip install -e .[dev]

You will need to install your operating system's FFTW3 development library.
You might need to `pip install extension_helpers` if there is an error about it being missing.

You can run::

    $ python setup.py build_ext --inplace

to build the C extension in place.

Code of Conduct
===============

When you are interacting with the SunPy community you are required to follow our `Code of Conduct.`_

License
=======

This project is Copyright (c) The SunPy Developers and licensed under the terms of the LGPL-2.1 license.
This package is based upon the `Openastronomy packaging guide <https://github.com/OpenAstronomy/packaging-guide>`__ which is licensed under the BSD 3-clause licence.

.. _`Developer's Guide`: https://docs.sunpy.org/en/latest/dev_guide/index.html
.. _`#sunpy:matrix.org`: https://riot.im/app/#/room/#sunpy:matrix.org
.. _issues page: https://github.com/sunpy/pyflct/issues
.. _contributing guide: https://docs.sunpy.org/en/latest/dev_guide/newcomers.html#newcomers
.. _Code of Conduct.: https://docs.sunpy.org/en/stable/coc.html
