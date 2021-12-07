## Preamble
"""
# Program: RotateAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Nov 4 00:21:50 2021
# Date Modified: Dec 7 2021
# Purpose: Run IMOD newstack -rotate command to rotate image stacks by a
degree value consistent with cross product. Defaults to 90 degree rotation.
# Imports: sys, os (operating system), and subprocess.
# Inputs/Arguments: Image stack .st dataset directory path and optional
rotation angle. If no angle is supplied, 90 degrees is chosen.
# Outputs/Returns: Rotated image stack located within original location.
Original image file renamed to <original>~ in same directory.
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


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    RotateAutomator()

# M02 End Program