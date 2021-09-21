## Preamble
"""
# Program: BinVolumeAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Mon Sep 13 16:24:01 2021
# Date Modified: Sep 21 2021
# Purpose: Run IMOD binvol command to isotropically bin tomogram
reconstructions by an optional argument. Defaults to a bin of 2.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Non-optional .mrc image data directory path. Optional 
binning dimension specification.
# Outputs/Returns: Binned .mrc of original tomogram reconstruction.
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
    regEx = ['([a-zA-Z0-9-]*)[_]','([0-9]+)[_]?','([a-z0-9-]*)',
             '[.]([a-zA-Z]*)']
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
    
    # Define Output Variables
    if dataInfo[0][0] == "":
        base = "Data"
    else:
        base = dataInfo[0][0]
    navID = dataInfo[0][1]
        
    inputSuffix = "rec"
    outputSuffix = f"{inputSuffix}-b{binSelect}"
    extension = "mrc"
    
    tomoInputFileName = f"{base}_{navID}_{inputSuffix}.{extension}"
    tomoOutputFileName = f"{base}_{navID}_{outputSuffix}.{extension}"
    
    tomoInputFilePath = os.path.join(inputPath,tomoInputFileName)
    tomoOutputFilePath = os.path.join(inputPath,tomoOutputFileName)
    
    # Control IMOD binvol Function
    os.chdir(inputPath)
    newstackCommand = " ".join(["binvol","-b",str(binSelect),
                                "-i",tomoInputFilePath,
                                "-o",tomoOutputFilePath])
    sp.run(newstackCommand,shell=True)


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    BinVolumeAutomator()

# M02 End Program