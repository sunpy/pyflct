import os
import re
import glob
import fnmatch

import pyflct

__all__ = ["rootdir", "file_list", "get_test_filepath", "test_data_filenames"]

rootdir = os.path.join(os.path.dirname(pyflct.__file__), "data")
file_list = glob.glob(os.path.join(rootdir, "*.[!p]*"))


def test_data_filenames():
    """
    Return a list of all test files in ``data`` directory.

    This ignores any ``py``, ``pyc`` and ``__*__`` files in these directories.

    Return
    ------
    get_all_test_filepath : `list`
        The name of all test files in ``data/test`` directory.
    """
    test_data_filenames_list = []
    excludes = ["*.pyc", "*" + os.path.sep + "__*__", "*.py"]
    excludes = r"|".join([fnmatch.translate(x) for x in excludes]) or r"$."

    for root, dirs, files in os.walk(rootdir):
        files = [os.path.join(root, f) for f in files]
        files = [f for f in files if not re.match(excludes, f)]
        files = [file.replace(rootdir + os.path.sep, "") for file in files]
        test_data_filenames_list.extend(files)

    return test_data_filenames_list


def get_test_filepath(filename, **kwargs):
    """
    Return the full path to a test file in the ``data`` directory.

    Parameters
    ----------
    filename : `str`
        The name of the file inside the ``data`` directory.

    Return
    ------
    filepath : `str`
        The full path to the file.

    Notes
    -----
    """
    files = test_data_filenames()
    return os.path.join(rootdir, files[[i for i, elem in enumerate(files) if filename in elem][0]])
