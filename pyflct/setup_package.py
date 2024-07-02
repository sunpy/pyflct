import os
import sys
import subprocess
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
    if sys.platform not in ["win32", "darwin"]:
        cfg["libraries"].append("fftw3")
    if get_compiler() == "msvc":
        # Anaconda paths
        cfg["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
        cfg["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))
    else:
        cfg["libraries"].append("m")
        if sys.platform == "darwin":
            brew_path = (
                subprocess.run(["brew", "--prefix"], stdout=subprocess.PIPE).stdout.decode("utf-8").replace("\n", "")
            )
            cfg["include_dirs"].append(f"{brew_path}/include/")
        cfg["include_dirs"].append("/usr/include/")
        cfg["extra_compile_args"].extend(["-O3", "-w", "-fomit-frame-pointer", "-fPIC"])
    return [Extension("pyflct._flct", **cfg)]
