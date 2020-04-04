# Licensed under GNU Lesser General Public License, version 2.1 - see licenses/LICENSE_FLCT.rst
from .flct import *
from .utils import *

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"
