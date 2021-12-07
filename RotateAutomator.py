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
    import os
    import subprocess as sp
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/Rotate"
    angleSelect = 90
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        angleSelect = int(sys.argv[2])
    else:
        angleSelect = 90
    
    # Acquire Subdirectories From Directory
    dataDirectory = os.chdir(inputPath)
    dataPartitions = os.listdir(dataDirectory)
    
    # Define Output Variables
    nameScheme =  lambda navID: f"{navID}/Tomo/tilt{navID}.st"
    imageStacks = []
    for partition in dataPartitions:
        imageStacks.append(nameScheme(partition))
    
    # Control IMOD newstack -rotate Function
    for imagePath in imageStacks:
        rotateCommand = " ".join(["newstack","-rotate",str(angleSelect),
                                "-in",imagePath,"-ou",imagePath])
        sp.run(rotateCommand,shell=True)
        # Clean Autosave Files
        sp.run("rm *~",shell=True)


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    RotateAutomator()

# M02 End Program