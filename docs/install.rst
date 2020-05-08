=======
Install
=======

Linux and Mac OS
----------------

The simplest way to install this library is through pip::

    $ pip install pyflct

This will install the pre-compiled binary wheels for these two platforms.

You can also install it through `Anaconda`_ using the command below used for Windows.

Windows
-------

We only officially support Windows through `Anaconda`_.

    $ conda install -c conda-forge pyflct

This uses the `conda-forge <https://conda-forge.org/>`__ channel.

Source Install
--------------

If you want to install the source only version of pyflct you will need to compile the C extension.
This means you will need a compiler ("gcc" or "MSVC") and the FFTW library installed.

Linux
^^^^^

Install FFTW from your distribution's repositories (some examples)::

    $ apt install libfftw3-dev
    $ pacman -S fftw3
    $ zypper install fftw3-devel

Now you install pyfftw from pip::

    $ pip install --no-binary pyfftw

Mac OS
^^^^^^

Install FFTW from `homebrew <http://brew.sh>`__::

    $ brew install fftw

Set these environmental variables::

    $ export LDFLAGS="-L/usr/local/lib"
    $ export CFLAGS="-I/usr/local/include"

Now you install pyfftw from pip::

    $ pip install --no-binary pyfftw

Windows
^^^^^^^

This is much more involved and we strongly suggest not doing this.

Common Steps
************

Set up the build environment with MSVC:

* Download `Build Tools for Visual Studio 2019 <https://visualstudio.microsoft.com/downloads/>`__.
* Install, making sure to check the option "C++ build tools" in the installer.

Anaconda
********

Set up FFTW::

    $ conda install fftw

Now you install pyfftw from pip::

    $ pip install pyfftw

Full source
***********

Set up FFTW:

* Download ZIP file of `precompiled FFTW Windows DLLs <http://www.fftw.org/install/windows.html>`__ and extract contents to a folder.
* Open the application "Developer Command Prompt for VS2019", change to the above folder, and run the following commands to create the import libraries (`libfftw3*.lib`)

.. code-block:: console

    lib /def:libfftw3-3.def /machine:x64
    lib /def:libfftw3f-3.def /machine:x64
    lib /def:libfftw3l-3.def /machine:x64

* Copy the `libfftw3*.dll` files to somewhere in `%PATH%` (or add the FFTW folder to `%PATH%`).
  `How to here. <https://stackoverflow.com/a/44272417>`__

* Modify `pyflct/setup_package.py` if not already modified so that the compilation options include the FFTW folder for `include_dirs` and `library_dirs` and the library names for `libraries`.

.. Anaconda: https://www.anaconda.com/products/individual
