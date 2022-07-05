## Preamble
"""
# Program: ModelStalker.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Tue Jul  5 16:35:28 2022
# Date Modified: Jul 5 2022
# Purpose: Perform stalking on all models located within given directory.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Tomogram dataset directory path. Works with additional 
files in directory and will generate files even if run more than once.
# Outputs/Returns: A stalked initial motive list for PEET processing.
"""

## Articles

def ModelStalker(inputPath):
    import re
    import os
    import subprocess as sp    
    
    # Regular Expression And Parsing Format:
    # Filename Format: tilt<NavID>_Suffix.Extension
    mainRegEx = ['tilt','([0-9]+)[_]?','([a-zA-Z0-9-_]*?)','(?:_s([0-9]*))?',
             '[.](mod)']
    mainPatternFinder = re.compile(''.join(mainRegEx))
    
    # Acquire Image Files From Directory
    dataDirectory = os.chdir(inputPath)
    allFiles = os.listdir(dataDirectory)
    
    imageInfo = []
    imageFiles = []
    for file in allFiles:
        try:
            metaInfo = mainPatternFinder.findall(file)[0]
            if metaInfo[2] == '':
                imageInfo.append(metaInfo)
                imageFiles.append(file)
        except IndexError:
            # No Computation Time Dedicated To Non-Scheme Files
            pass
    
    # Control IMOD/PEET stalkInit Function
    for file in imageFiles:
        stalkCommand = " ".join(["stalkInit",file])
        sp.run(stalkCommand,shell=True)
    
    # Remove Overwrritten Files
    os.remove("head.mod")
    os.remove("tail.mod")
    os.remove("centroid.mod")


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/TemplateProcessing"
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    
    # Main Script Run
    ModelStalker(inputPath)

# M02 End Program