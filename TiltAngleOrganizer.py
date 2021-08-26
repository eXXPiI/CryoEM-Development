## Preamble
"""
# Program: TiltAngleOrganizer.py
# Version: 0.1.0
# Author: Jonathan Myers
# Date: Mon Aug 23 16:53:57 2021
# Purpose: Builds angle sorted image stack of form .st from .mrc images of 
tomography samples for IMOD tomogram reconstruction.
# Imports: re (regular expression) and os (operating system).
# Inputs/Arguments: Optional .mrc image data directory path or default working
directory path.
# Outputs/Returns: Angle sorted stack (.st) in optional directory path or
image data directory.
"""

## Articles

# Regular Expression Finder
import re
import os
#import subprocess as sp

# Regular Expression:
dataDirectory = os.getcwd()
dataFiles = os.listdir(dataDirectory)

regEx = '([a-zA-Z0-9]*[_])? \
    ([0-9]+)[_] \
    ([-]?[0-9]+[\.][0-9]+)[_] \
    ([a-zA-Z0-9]+)[_] \
    ([0-9]+[.][0-9]+[.][0-9]+)'
patternFinder = re.compile(regEx)