import os
import sys
import platform
import subprocess
from glob import glob
from collections import defaultdict
from distutils.core import Extension

import numpy as np
from extension_helpers import get_compiler

ROOT = os.path.dirname(__file__)

BREW_PATHS = ["brew", "/usr/local/conda_mangled/sbin/brew"]


def get_extensions():
    cfg = defaultdict(list)
    cfg["include_dirs"].append(np.get_include())
    cfg["include_dirs"].append(os.path.join("cextern"))
    cfg["sources"].extend(sorted(glob(os.path.join("cextern", "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "flct.pyx"))))
    cfg["libraries"].append("fftw3")
    # Conda paths
    cfg["include_dirs"].append(os.path.join(sys.base_prefix, "Library", "include"))
    cfg["library_dirs"].append(os.path.join(sys.base_prefix, "Library", "lib"))
    if get_compiler().lower() == "msvc":
        cfg["extra_compile_args"].extend(["/w"])
    else:
        cfg["libraries"].append("m")
        # We assume we have brew installed on Mac OS to provide FFTW3
        # If not, we add system paths as well as the conda-forge paths
        # hoping that the user has installed FFTW3 there.
        if platform.system().lower() == "darwin":
            for brew_path in BREW_PATHS:
                try:
                    brew_path = (
                        subprocess.run([brew_path, "--prefix"], stdout=subprocess.PIPE)
                        .stdout.decode("utf-8")
                        .replace("\n", "")
                    )
                    cfg["include_dirs"].append(f"{brew_path}/include")
                    break
                except FileNotFoundError:
                    continue
        # System paths
        cfg["include_dirs"].append(os.path.join(sys.prefix, "include"))
        cfg["include_dirs"].append(os.path.join(sys.prefix, "local", "include"))
        cfg["extra_compile_args"].extend(["-O3", "-w", "-fomit-frame-pointer", "-fPIC"])
    return [Extension("pyflct._flct", **cfg)]
