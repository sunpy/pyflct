from .flct import *  # NOQA

try:
    from .version import __version__
except ImportError:
    __version__ = "unknown"
