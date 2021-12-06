## Preamble
"""
# Program: RotateAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Nov 4 00:21:50 2021
# Date Modified: Nov 4 2021
# Purpose: None.
# Imports: None.
# Inputs/Arguments: None.
# Outputs/Returns: None.
"""

## Articles

def RotateAutomator():
    import sys
    import re
    import os
    import subprocess as sp
    
    # Testing/Debugging Lines
    #"""
    inputPath = "/home/jmyers/Documents/testFolder/Rotate"
    angleSelect = 90
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        angleSelect = int(sys.argv[2])
    else:
        angleSelect = 90
    """
    
    # Regular Expression And Parsing Format:
    # emClarity Format: tilt<NavID>.st
    emClarityRegEx = ['tilt','([0-9]+)','.st']
    emClarityPatternFinder = re.compile(''.join(emClarityRegEx))
    # Base Format: Base_NavID.txt (If Ever Useful)
    #txtRegEx = ['([a-zA-Z0-9-]*)[_]','([0-9]+)[_]?','.txt']
    #txtPatternFinder = re.compile(''.join(txtRegEx))
    
    # Acquire Subdirectories From Directory
    dataDirectory = os.chdir(inputPath)
    dataPartitions = os.listdir(dataDirectory)
    dataFiles = []
    for partition in dataPartitions:
        internalPath = f"{partition}/Tomo"
        dataFiles.append(os.listdir(internalPath))
    
    # Parse Files in Subdirectories For Stacks
    imageStacks = []
    for fileList in dataFiles:
        for file in fileList:
            try:
                imageStacks.append(emClarityPatternFinder.findall(file)[0])
            except IndexError:
                # No Computation Time Dedicated To Non-Scheme Files
                pass
    
    # Define Output Variables
    nameScheme =  lambda navID: f"tilt{navID}.st"
    oldImageStacks = []
    newImageStacks = []
    for partition in dataPartitions:
        
    
    # Control IMOD newstack -rotate Function
    
    print("done")

# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    RotateAutomator()

# M02 End Program