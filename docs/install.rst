=======
Install
=======

We recommend the release on the python package index with tools such as pip::

    $ pip install pyflct

Hopefully we will have pre-built binary wheels for Linux nad Mac OS X in the near future.
Note we do not support Windows the current time.

Installation from PyPI may also work on other systems when the FFTW libraries
are available, but other platforms have not been tested.

Hopefully users of the `conda <https://conda.io/docs/>`__ package manager can install from the `conda-forge <https://conda-forge.org/>`__ channel via::

    $ conda install -c conda-forge pyflct

in the near future.

Until then you will need to have the FFTW libraries installed on your computer.

Linux
-----

Install FFTW from your distrubtion's repositories::

    $ apt install libfftw3-dev

or::

    $ pacman -S fftw3

or::

    $ zypper install fftw3-devel

Now install pyfftw from pip::

    $ pip install pyfftw

Mac OS X
--------

Install FFTW from [homebrew](http://brew.sh>)::

    $ brew install fftw

Set these environmental variables::

    $ export LDFLAGS="-L/usr/local/lib"
    $ export CFLAGS="-I/usr/local/include"

Now install pyfftw from pip::

    $ pip install pyfftw
