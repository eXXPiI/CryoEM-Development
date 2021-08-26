## Preamble
"""
# Program: TiltAngleOrganizer.py
# Version: 0.1.0
# Author: Jonathan Myers
# Date Created: Mon Aug 23 16:53:57 2021
# Date Modified: Aug 26 2021
# Purpose: Builds angle sorted image stack of form .st from .mrc images of 
tomography samples for IMOD tomogram reconstruction.
# Imports: re (regular expression) and os (operating system).
# Inputs/Arguments: Optional .mrc image data directory path or default working
directory path.
# Outputs/Returns: Angle sorted stack (.st) in optional directory path or
image data directory.
"""

# Articles

def TiltAngleOrganizer():
    #%%
    import re
    import os
    import subprocess as sp
    
    # Regular Expression:
    regEx = ['([a-zA-Z0-9-]*[_])?','([0-9]+)[_]','([-]?[0-9]+[\.][0-9]+)[_]',
             '([a-zA-Z0-9]+)[_]','([0-9]+[\.][0-9]+[\.][0-9]+)']
    patternFinder = re.compile(''.join(regEx))
    
    # Acquire Files From Directory
    cwd = os.getcwd()
    dataDirectory = os.chdir("../test")
    dataFiles = os.listdir(dataDirectory)
    dataLen = len(dataFiles)
    
    # Mine Filename Metadata
    dataInfo = []
    for i in range(dataLen):
        dataInfo.append(patternFinder.findall(dataFiles[i])[0])
    
    # Sort Files On Angle
    angles = [float(val[2]) for val in dataInfo]
    sortedAngleIndex = sorted(range(dataLen),key=lambda x:angles[x])
    sortedFiles = [dataFiles[index] for index in sortedAngleIndex]
    
    # Write To Text File For IMOD
    imodInputFile = open("sortedAngles.txt", 'w')
    imodInputFile.write(str(dataLen))
    imodInputFile.write("\n")
    for index in range(dataLen):
        imodInputFile.write(sortedFiles[index])
        imodInputFile.write("\n")
    imodInputFile.close()
    
    # Control IMOD newstack Function
    
    #%%

# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    TiltAngleOrganizer()

# M02 End Program
