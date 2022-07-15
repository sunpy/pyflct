import os
import sys
from glob import glob
from collections import defaultdict
from distutils.core import Extension

import numpy as np
from extension_helpers import get_compiler

ROOT = os.path.dirname(__file__)


def get_extensions():
    cfg = defaultdict(list)
    cfg["include_dirs"].append(np.get_include())
    cfg["include_dirs"].append(os.path.join(sys.prefix, "include"))
    cfg["include_dirs"].append(os.path.join("cextern"))
    cfg["sources"].extend(sorted(glob(os.path.join("cextern", "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "flct.pyx"))))
    cfg["libraries"].append("fftw3")
    if sys.platform == "win32":
        cfg["include_dirs"].append(os.path.join("cextern","windows"))
        cfg["libraries"].append(os.path.join(sys.prefix, 'bin'))
    if get_compiler() != "msvc":
        cfg["libraries"].append("m")
        cfg["include_dirs"].append("/usr/include/")
        cfg["extra_compile_args"].extend(["-O3", "-Wall", "-fomit-frame-pointer", "-fPIC"])

    return [Extension("pyflct._flct", **cfg)]
