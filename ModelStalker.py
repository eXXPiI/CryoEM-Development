## Preamble
"""
# Program: ModelStalker.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Tue Jul  5 16:35:28 2022
# Date Modified: Jul 6 2022
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
    mainRegEx = ['tilt','([0-9]+)[_]?','([a-zA-Z0-9-_]*?)',
             '(head|tail|centroid)?','[.](mod)']
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
            else:
                os.remove(file)
        except IndexError:
            # No Computation Time Dedicated To Non-Scheme Files
            pass
    
    # Set Model Output Filenames
    imageFileNumber = len(imageFiles)
    nameScheme =  lambda navID,suffix,pointType: f"tilt{navID}_{suffix}_{pointType}.mod"
    
    outputModels = []
    for i in range(imageFileNumber):
        individualModels = []
        individualModels.append(nameScheme(imageInfo[i][0],imageInfo[i][1],"head"))
        individualModels.append(nameScheme(imageInfo[i][0],imageInfo[i][1],"tail"))
        individualModels.append(nameScheme(imageInfo[i][0],imageInfo[i][1],"centroid"))
        outputModels.append(individualModels)
    
    # Control IMOD/PEET stalkInit Function
    for i in range(imageFileNumber):
        stalkCommand = " ".join(["stalkInit",imageFiles[i]])
        sp.run(stalkCommand,shell=True)
        # Rename Main Model Outputs
        os.rename("head.mod",outputModels[i][0])
        os.rename("tail.mod",outputModels[i][1])
        os.rename("centroid.mod",outputModels[i][2])


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