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

def get_extensions():
    cfg = defaultdict(list)
    cfg["include_dirs"].append(np.get_include())
    cfg["include_dirs"].append(os.path.join("cextern"))
    cfg["sources"].extend(sorted(glob(os.path.join("cextern", "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "*.c"))))
    cfg["sources"].extend(sorted(glob(os.path.join(ROOT, "flct.pyx"))))
    cfg["libraries"].append("fftw3")
    if get_compiler().lower() == "msvc":
        # Conda paths based on sys.base_prefix
        cfg["include_dirs"].append(os.path.join(sys.base_prefix, "Library", "include"))
        cfg["library_dirs"].append(os.path.join(sys.base_prefix, "Library", "lib"))
        cfg["extra_compile_args"].extend(["/w"])
    else:
        cfg["libraries"].append("m")
        # We assume we have brew installed on Mac OS to provide FFTW3
        if platform.system().lower() == "darwin":
            try:
                brew_path = (
                    subprocess.run(["brew", "--prefix"], stdout=subprocess.PIPE)
                    .stdout.decode("utf-8")
                    .replace("\n", "")
                )
            except FileNotFoundError:
                # If we are on conda-forge build environment, we need to use the conda_mangled brew
                brew_path = (
                    subprocess.run(["/usr/local/conda_mangled/sbin/brew", "--prefix"], stdout=subprocess.PIPE)
                    .stdout.decode("utf-8")
                    .replace("\n", "")
                )
            cfg["include_dirs"].append(f"{brew_path}/include")
        cfg["include_dirs"].append(os.path.join(sys.prefix, "include"))
        cfg["include_dirs"].append(os.path.join(sys.prefix, "local", "include"))
        cfg["extra_compile_args"].extend(["-O3", "-w", "-fomit-frame-pointer", "-fPIC"])
    return [Extension("pyflct._flct", **cfg)]
