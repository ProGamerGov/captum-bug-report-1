#!/usr/bin/env python3

# Welcome to the PyTorch Captum setup.py.

import os
import re
import subprocess
import sys

from setuptools import find_packages, setup

REQUIRED_MAJOR = 3
REQUIRED_MINOR = 6

# Check for python version
if sys.version_info < (REQUIRED_MAJOR, REQUIRED_MINOR):
    error = (
        "Your version of python ({major}.{minor}) is too old. You need "
        "python >= {required_major}.{required_minor}."
    ).format(
        major=sys.version_info.major,
        minor=sys.version_info.minor,
        required_minor=REQUIRED_MINOR,
        required_major=REQUIRED_MAJOR,
    )
    sys.exit(error)


# Allow for environment variable checks
def check_env_flag(name, default=""):
    return os.getenv(name, default).upper() in ["ON", "1", "YES", "TRUE", "Y"]


BUILD_INSIGHTS = check_env_flag("BUILD_INSIGHTS")
VERBOSE_SCRIPT = True
for arg in sys.argv:
    if arg == "-q" or arg == "--quiet":
        VERBOSE_SCRIPT = False


def report(*args):
    if VERBOSE_SCRIPT:
        print(*args)
    else:
        pass


# get version string from module
with open(os.path.join(os.path.dirname(__file__), "captum/__init__.py"), "r") as f:
    version = re.search(r"__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M).group(1)
    report("-- Building version " + version)

# read in README.md as the long description
with open("README.md", "r") as fh:
    long_description = fh.read()


# explore paths under root and subdirs to gather package files
def get_package_files(root, subdirs):
    paths = []
    for subroot in subdirs:
        paths.append(os.path.join(subroot, "*"))
        for path, dirs, _ in os.walk(os.path.join(root, subroot)):
            for d in dirs:
                paths.append(os.path.join(path, d, "*")[len(root) + 1 :])
    return paths


if __name__ == "__main__":

    setup(
        name="captum",
        version=version,
        description="Model interpretability for PyTorch",
        author="PyTorch Team",
        license="BSD-3",
        url="https://captum.ai",
        project_urls={
            "Documentation": "https://captum.ai",
            "Source": "https://github.com/pytorch/captum",
            "conda": "https://anaconda.org/pytorch/captum",
        },
        keywords=[
            "Model Interpretability",
            "Model Understanding",
            "Feature Importance",
            "Neuron Importance",
            "PyTorch",
        ],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Developers",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: BSD License",
            "Programming Language :: Python :: 3 :: Only",
            "Topic :: Scientific/Engineering",
        ],
        long_description=long_description,
        long_description_content_type="text/markdown",
        python_requires=">=3.6",
        install_requires=["packaging"],
        packages=find_packages(exclude=("tests", "tests.*")),
    )
