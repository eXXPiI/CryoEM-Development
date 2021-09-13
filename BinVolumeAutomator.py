## Preamble
"""
# Program: BinVolumeAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Mon Sep 13 16:24:01 2021
# Date Modified: Sep 13 2021
# Purpose: Run IMOD binvol command to bin tomograms to full 
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles

def BinVolumeAutomator():
    import sys
    import re
    import os
    import subprocess as sp
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        binSelect = int(sys.argv[2])
    else:
        binSelect = 2
    
    # Regular Expression:
    regEx = ['([a-zA-Z0-9-]*[_])?','([0-9]+)[_]','([a-zA-Z0-9]+)[_]','([0-9]+[\.][0-9]+[\.][0-9]+)']
    patternFinder = re.compile(''.join(regEx))
    
    # Acquire Files From Directory
    #dataDirectory = os.getcwd()
    dataDirectory = os.chdir(inputPath)
    dataFiles = os.listdir(dataDirectory)
    dataLen = len(dataFiles)
    
    # Mine Filename Metadata
    dataInfo = []
    for i in range(dataLen):
        dataInfo.append(patternFinder.findall(dataFiles[i])[0])

# M02 End Program