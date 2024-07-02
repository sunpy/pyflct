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

    if get_compiler().lower() == "msvc":
        # Anaconda paths
        cfg["include_dirs"].append(os.path.join(sys.prefix, "Library", "include"))
        cfg["library_dirs"].append(os.path.join(sys.prefix, "Library", "lib"))
    else:
        cfg["libraries"].append("m")
        # WE assume we have brew installed on Mac OS to provide FFTW3
        if sys.platform.lower() == "darwin":
            brew_path = (
                subprocess.run(["brew", "--prefix"], stdout=subprocess.PIPE).stdout.decode("utf-8").replace("\n", "")
            )
            cfg["include_dirs"].append(f"{brew_path}/include")
        if not (sys.platform.lower() == "darwin" and sys.processor().lower() == "arm"):
            # This does not get registered on ARM Mac via Brew
            cfg["libraries"].append("fftw3")
        cfg["include_dirs"].append("/usr/include")
        cfg["extra_compile_args"].extend(["-O3", "-w", "-fomit-frame-pointer", "-fPIC"])
    return [Extension("pyflct._flct", **cfg)]
