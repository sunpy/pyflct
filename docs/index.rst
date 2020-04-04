********************
pyflct Documentation
********************

This is the documentation for pyflct.

pyflct contains routines which can be used to perform Fourier Local Correlation Tracking (FLCT).
Wrapping a C-based implementation of the FLCT algorithm developed by George H. Fisher and Brian T. Welsch (who we would like to thank for letting us include it).
`The C source code can be found here <http://cgem.ssl.berkeley.edu/cgi-bin/cgem/FLCT/home>`__.

The following papers are references for the FLCT algorithm:

* `Welsch et al., ApJ 610, 1148, (2004) <https://iopscience.iop.org/article/10.1086/421767>`__
* `Fisher & Welsch, PASP 383, 373, (2008) <https://arxiv.org/abs/0712.4289>`__
* `Fisher et al., ApJS, accepted (2020) <https://arxiv.org/abs/0712.4289>`__

.. note::
    The FLCT C source is licensed under the GNU Lesser General Public License, version 2.1, see ``cextern/COPYRIGHT``.

.. toctree::
   :maxdepth: 1

   install
   pyflct
   generated/gallery/index
   whatsnew/index
