# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config
# flake8: NOQA
import sys
try:
    from sphinx_astropy.conf.v1 import *
except ImportError:
    print("ERROR: the documentation requires the sphinx-astropy package to be installed")
    sys.exit(1)

# -- Project information -----------------------------------------------------
import os
from pyflct import __version__
project = "pyflct"
copyright = "2020, The SunPy Developers"
author = "The SunPy Developers"

# The full version, including alpha/beta/rc tags

release = __version__
is_development = ".dev" in __version__

try:
    import sphinx_gallery
    sphinx_gallery.__version__
    if on_rtd and os.environ.get("READTHEDOCS_PROJECT").lower() != "sunpy":
        # Gallery takes too long on RTD to build unless you have extra build time.
        has_sphinx_gallery = False
    else:
        has_sphinx_gallery = True
except ImportError:
    has_sphinx_gallery = False

if on_rtd:
    os.environ["SUNPY_CONFIGDIR"] = "/home/docs/"
    os.environ["HOME"] = "/home/docs/"
    os.environ["LANG"] = "C"
    os.environ["LC_ALL"] = "C"


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.coverage",
    "sphinx.ext.inheritance_diagram",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "sphinx.ext.doctest",
    "sphinx.ext.mathjax",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",
]

# Add any paths that contain templates here, relative to this directory.
# templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The reST default role (used for this markup: `text`) to use for all
# documents. Set to the "smart" one.
default_role = "obj"

# -- Options for intersphinx extension ---------------------------------------

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    "python": (
        "https://docs.python.org/3/",
        (None, "http://data.astropy.org/intersphinx/python3.inv"),
    ),
    "numpy": (
        "https://docs.scipy.org/doc/numpy/",
        (None, "http://data.astropy.org/intersphinx/numpy.inv"),
    ),
    "scipy": (
        "https://docs.scipy.org/doc/scipy/reference/",
        (None, "http://data.astropy.org/intersphinx/scipy.inv"),
    ),
    "matplotlib": (
        "https://matplotlib.org/",
        (None, "http://data.astropy.org/intersphinx/matplotlib.inv"),
    ),
    "astropy": ("http://docs.astropy.org/en/stable/", None),
    "sunpy": ("https://docs.sunpy.org/en/stable/", None),
}

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

try:
    from sunpy_sphinx_theme.conf import *
except ImportError:
    html_theme = "default"


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']

# Render inheritance diagrams in SVG
graphviz_output_format = "svg"

graphviz_dot_args = [
    "-Nfontsize=10",
    "-Nfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Efontsize=10",
    "-Efontname=Helvetica Neue, Helvetica, Arial, sans-serif",
    "-Gfontsize=10",
    "-Gfontname=Helvetica Neue, Helvetica, Arial, sans-serif",
]


"""
Write the latest changelog into the documentation.
"""
target_file = os.path.abspath("./whatsnew/latest_changelog.txt")
try:
    from sunpy.util.towncrier import generate_changelog_for_docs

    if is_development:
        generate_changelog_for_docs("../", target_file)
except Exception as e:
    print(f"Failed to add changelog to docs with error {e}.")
# Make sure the file exists or else sphinx will complain.
open(target_file, "a").close()

# -- Options for the Sphinx gallery -------------------------------------------
if has_sphinx_gallery:
    import pathlib

    extensions += ["sphinx_gallery.gen_gallery"]
    path = pathlib.Path.cwd()
    example_dir = path.parent.joinpath("examples")
    sphinx_gallery_conf = {
        "backreferences_dir": str(path.joinpath("generated", "modules")),
        "filename_pattern": "^((?!skip_).)*$",
        "examples_dirs": example_dir,
        "gallery_dirs": path.joinpath("generated", "gallery"),
        "default_thumb_file": path.joinpath("logo", "sunpy_icon_128x128.png"),
        "abort_on_example_error": False,
        "plot_gallery": True,
    }


def setup(app):
    if not has_sphinx_gallery:
        import warnings

        warnings.warn(
            "The sphinx_gallery extension is not installed, so the "
            "gallery will not be built. You will probably see "
            "additional warnings about undefined references due "
            "to this."
        )
