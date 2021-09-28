## Preamble
"""
# Program: TiltAngleOrganizer.py
# Version: 0.1.0
# Author: Jonathan Myers
# Date Created: Mon Aug 23 16:53:57 2021
# Date Modified: Aug 26 2021
# Purpose: Builds angle sorted image stack of form .st from .mrc images of 
tomography samples for IMOD tomogram reconstruction.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Non-optional .mrc image data directory path. Optional 
IMOD/Etomo start boolean for completed stack.
# Outputs/Returns: Angle sorted stack (.st) in optional directory path or
image data directory. Sorted angle .rawtlt file and sorted data intermediate file.
"""

# Articles

def TiltAngleOrganizer():
    import sys
    import re
    import os
    import subprocess as sp
    
    # Testing/Debugging Lines
    inputPath = "/home/jmyers/Documents/testFolder/Unique"
    etomoSelect = False
    
    # Define Input Variables
    """
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        etomoSelect = bool(int(sys.argv[2]))
    else:
        etomoSelect = False
    """
    
    # Regular Expression:
    regEx = ['([a-zA-Z0-9-]*[_])?','([0-9]+)[_]','([-]?[0-9]+[\.][0-9]+)[_]',
             '([a-zA-Z0-9]+)[_]','([0-9]+[\.][0-9]+[\.][0-9]+)']
    patternFinder = re.compile(''.join(regEx))
    baseLocation = 0
    navIDLocation = 1
    angleLocation = 2
    dateLocation = 3
    timeLocation = 4
    
    # Acquire Files From Directory
    dataDirectory = os.chdir(inputPath)
    dataFiles = os.listdir(dataDirectory)
    dataLen = len(dataFiles)
    
    # Mine Filename Metadata
    dataInfo = []
    for i in range(dataLen):
        dataInfo.append(patternFinder.findall(dataFiles[i])[0])
    
    # Determine Efficient Angle Sorting Routine
    angles = [float(val[angleLocation]) for val in dataInfo]
    anglesLen = len(angles)
    uniqueAngles = set(angles)
    angleNum = len(uniqueAngles)
    
    if anglesLen == angleNum:
        # Sort Files by Angle Without Latest Image Recording
        sortedAngleIndex = sorted(range(dataLen),key=lambda x:angles[x])
        sortedAngles = [dataInfo[index][angleLocation] for index in sortedAngleIndex]
        sortedFiles = [dataFiles[index] for index in sortedAngleIndex]
    else:
        # Sort Files by Angle Using Latest Image Recording
        print("hello")
        
    
    # Define Output Variables
    # Selects Information from First File
    if dataInfo[0][baseLocation] == "":
        base = "Data"
    else:
        base = dataInfo[0][baseLocation]
    navID = dataInfo[0][navIDLocation]
    
    dirName = "Tomo"
    imodInputFileName = f"{base}_{navID}.txt"
    tiltOutputFileName = f"{base}_{navID}.rawtlt"
    stackOutputFileName = f"{base}_{navID}.st"
    
    imodInputFilePath = os.path.join(inputPath,dirName,imodInputFileName)
    tiltOutputFilePath = os.path.join(inputPath,dirName,tiltOutputFileName)
    stackOutputFilePath = os.path.join(inputPath,dirName,stackOutputFileName)
    
    # Create Separate File Directory
    os.mkdir(dirName)
    os.chdir(dirName)
    
    # Write Raw Tilt File for IMOD/Etomo
    tiltOutputFile = open(tiltOutputFilePath,'w')
    tiltOutputFile.write("\n".join([str(a) for a in sortedAngles]))
    tiltOutputFile.close()
    
    # Write To Text File For IMOD
    imodInputFile = open(imodInputFilePath,'w')
    imodInputFile.write(str(angleNum))
    imodInputFile.write("\n")
    for index in range(angleNum):
        imodInputFile.write(sortedFiles[index])
        imodInputFile.write("\n")
        imodInputFile.write("/")
        imodInputFile.write("\n")
    imodInputFile.close()
    
    # Control IMOD newstack Function
    os.chdir(inputPath)
    newstackCommand = " ".join(["newstack","-filei",imodInputFilePath,
                                "-ou",stackOutputFilePath])
    sp.run(newstackCommand,shell=True)
    if etomoSelect == True:
        imodCommand = " ".join(["imod",stackOutputFilePath])
        sp.run(imodCommand,shell=True)
    
    
# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    TiltAngleOrganizer()

# M02 End Program
