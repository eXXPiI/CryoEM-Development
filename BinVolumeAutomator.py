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
    
    """# Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        binSelect = int(sys.argv[2])
    else:
        binSelect = 2
    """
    inputPath = "/home/jmyers/Documents/PEET_Projects/Janelia2018/TomoReplace/226"
    
    # Regular Expression:
    regEx = ['([a-zA-Z0-9-])*[_]','([0-9]+)[_]?','([a-z0-9-]*)',
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
    for i in range(dataLen):
        
    suffix = 
    
    dirName = "Processing"
    tomoInputFileName = f"{base}_{navID}_{suffix}.txt"
    tomoOutputFileName = f"{base}_{navID}.st"
    
    tomoInputFilePath = os.path.join(inputPath,dirName,tomoInputFileName)
    tomoOutputFilePath = os.path.join(inputPath,dirName,tomoOutputFileName)
    


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    BinVolumeAutomator()

# M02 End Program