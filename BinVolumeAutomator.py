## Preamble
"""
# Program: BinVolumeAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Mon Sep 13 16:24:01 2021
# Date Modified: Oct 19 2021
# Purpose: Run IMOD binvol command to isotropically bin tomogram
reconstructions by an optional argument. Defaults to a bin of 2.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Non-optional .mrc image data directory path. Optional 
binning dimension specification.
# Outputs/Returns: Binned .mrc of original tomogram reconstruction.
"""

## Articles

def BinVolumeAutomator(inputPath,binSelect):
    import re
    import os
    import subprocess as sp
    
    # Regular Expression And Parsing Format:
    # emClarity Format: tilt<NavID>_Suffix.Extension
    emClarityRegEx = ['tilt','([0-9]+)[_]?','([a-z0-9-]*)',
             '[.]([a-zA-Z]*)']
    emClarityPatternFinder = re.compile(''.join(emClarityRegEx))
    # Base Format: Base_NavID.txt (If Ever Useful)
    #txtRegEx = ['([a-zA-Z0-9-]*)[_]','([0-9]+)[_]?','.txt']
    #txtPatternFinder = re.compile(''.join(txtRegEx))
    
    # Acquire Files From Directory and Parse Filename Metadata
    dataDirectory = os.chdir(inputPath)
    dataFiles = os.listdir(dataDirectory)
    dataInfo = []
    for info in dataFiles:
        try:
            dataInfo.append(emClarityPatternFinder.findall(info)[0])
        except IndexError:
            # No Computation Time Dedicated To Non-Scheme Files
            pass
    
    # Define Output Variables
    # Selects Information From First File
    navID = dataInfo[0][0]
    inputSuffix = "rec"
    outputSuffix = f"{inputSuffix}-bin{binSelect}"
    inputExtension = "mrc"
    outputExtension = "mrc"
    
    tomoInputFileName = f"tilt{navID}_{inputSuffix}.{inputExtension}"
    tomoOutputFileName = f"tilt{navID}_{outputSuffix}.{outputExtension}"
    
    tomoInputFilePath = os.path.join(inputPath,tomoInputFileName)
    tomoOutputFilePath = os.path.join(inputPath,tomoOutputFileName)
    
    # Control IMOD binvol Function
    os.chdir(inputPath)
    binvolCommand = " ".join(["binvol","-b",str(binSelect),
                                "-i",tomoInputFilePath,
                                "-o",tomoOutputFilePath])
    sp.run(binvolCommand,shell=True)


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/PNCC_Format/Tomo"
    binSelect = 2
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        binSelect = int(sys.argv[2])
    else:
        binSelect = 2
    
    # Main Script Run
    BinVolumeAutomator(inputPath,binSelect)

# M02 End Program