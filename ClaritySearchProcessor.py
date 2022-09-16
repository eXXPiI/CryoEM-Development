## Preamble
"""
# Program: ClaritySearchProcessor.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Jun 23 14:57:49 2022
# Date Modified: Aug 11 2022
# Purpose: Flip pixel values from emClarity output and process using
TomoSegMemTV script scale_space to enhance image clarity.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Tomogram dataset directory path and optional s-value for 
image enhancement. If no value is supplied, 1 is chosen. Works with additional 
files in directory and will generate files even if run more than once. Non-positive
s-value results in no scale space performed.
# Outputs/Returns: A pixel inverted tomogram file with contrast enhancement.
"""

## Articles

def ClaritySearchProcessor(inputPath,sValueSelect):
    import re
    import os
    import subprocess as sp    
    
    # Regular Expression And Parsing Format:
    # Filename Format: tilt<NavID>_Suffix.Extension
    mainRegEx = ['tilt','([0-9]+)[_]?','([a-zA-Z0-9-_]*?)','(?:_s([0-9]*))?',
             '[.](mrc|rec)']
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
    
    # Set Output Filenames
    imageFileNumber = len(imageFiles)
    nameScheme =  lambda navID,suffix,sValue: f"tilt{navID}_{suffix}_s{sValue}.rec"
    
    outputImages = []
    for i in range(imageFileNumber):
        outputImages.append(nameScheme(imageInfo[i][0],imageInfo[i][1],sValueSelect))
    
    # Control IMOD newstack -multadd Function
    for i in range(imageFileNumber):
        invertCommand = " ".join(["newstack","-multadd","-1,0",
                                "-in",imageFiles[i],"-ou",outputImages[i]])
        sp.run(invertCommand,shell=True)
    
    if sValueSelect < 0:
        for i in range(imageFileNumber):
            enhanceCommand = " ".join(["scale_space","-s",str(sValueSelect),
                                       outputImages[i],outputImages[i]])
            sp.run(enhanceCommand,shell=True)
        

# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/TemplateProcessing"
    sValueSelect = 1
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        sValueSelect = int(sys.argv[2])
    else:
        sValueSelect = 1
    
    # Main Script Run
    ClaritySearchProcessor(inputPath,sValueSelect)

# M02 End Program