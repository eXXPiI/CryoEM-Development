## Preamble
"""
# Program: TiltAngleOrganizer.py
# Version: 0.1.0
# Author: Jonathan Myers
# Date Created: Mon Aug 23 16:53:57 2021
# Date Modified: Oct 18 2021
# Purpose: Builds angle sorted image stack of form .st from .mrc images of 
tomography samples for IMOD tomogram reconstruction.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Non-optional global .mrc image data directory path. Optional 
IMOD/Etomo start boolean for completed stack.
# Outputs/Returns: Angle sorted stack (.st) in optional directory path or
image data directory. Sorted angle .rawtlt file and sorted data intermediate file.
"""

## Articles

def TiltAngleOrganizer():
    import sys
    import re
    import os
    import datetime as dt
    import subprocess as sp
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/PNCC_Format"
    etomoSelect = False
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    if len(sys.argv) == 3:
        etomoSelect = bool(int(sys.argv[2]))
    else:
        etomoSelect = False
    
    # Regular Expression and Parsing Format:
    # PNCC/SerialEM Format: Base_GridNum_NavID_ImageNum_Angle_<Date_Time>.Extension (0245)
    regEx = ['(?:([a-zA-Z0-9-]*)[_])?','(?:([0-9])[_])?','([0-9]+)[_]',
             '(?:([0-9]{5})[_])?','([-]?[0-9]+[\.][0-9]+)[_]',
             '([a-zA-Z0-9]+[_][0-9]+[\.][0-9]+[\.][0-9]+)']
    patternFinder = re.compile(''.join(regEx))
    baseLocation = 0
    navIDLocation = 2
    angleLocation = 4
    timeLocation = 5
    parseFormat = "%b%d_%H.%M.%S"

    # Acquire Files From Directory And Create Output Directory If Not Existent
    newDirName = "Tomo"
    dataDirectory = os.chdir(inputPath)
    dataFiles = os.listdir(dataDirectory)
    if dataFiles.count(newDirName) > 0:
        dataFiles.remove(newDirName)
    else:
        os.mkdir(newDirName)
    dataLen = len(dataFiles)
    
    # Parse Filename Metadata
    dataInfo = []
    for i in range(dataLen):
        dataInfo.append(patternFinder.findall(dataFiles[i])[0])

    # Extract All Image Dates
    allDates = []
    for i in range(dataLen):
        allDates.append(dt.datetime.strptime(dataInfo[i][timeLocation],parseFormat))
    
    # Determine Efficient Angle Sorting Routine
    allAngles = [float(val[angleLocation]) for val in dataInfo]
    uniqueAngles = sorted(set(allAngles))
    angleNum = len(uniqueAngles)
    
    # Run Efficient Sorting Routine
    if dataLen == angleNum:
        # Sort Files by Angle Without Latest Image Recording
        sortedAngleIndex = sorted(range(dataLen),key=lambda x:allAngles[x])
    else:
        # Sort Files by Angle Using Latest Image Recording
        sortedAngleIndex = []
        for uniqueAngle in uniqueAngles:
            angleIndices = [index for index,angle in enumerate(allAngles) if angle == uniqueAngle]
            angleDates = [allDates[index] for index in angleIndices]
            sortedAngleIndex.append(allDates.index(max(angleDates)))
    sortedFiles = [dataFiles[index] for index in sortedAngleIndex]
    
    # Define Output Variables
    # Selects Information from First File
    if dataInfo[0][baseLocation] == "":
        base = "Data"
    else:
        base = dataInfo[0][baseLocation]
    navID = dataInfo[0][navIDLocation]
    
    imodInputFileName = f"{base}_{navID}.txt"
    tiltOutputFileName = f"tilt{navID}.rawtlt"
    stackOutputFileName = f"tilt{navID}.st"
    
    imodInputFilePath = os.path.join(inputPath,newDirName,imodInputFileName)
    tiltOutputFilePath = os.path.join(inputPath,newDirName,tiltOutputFileName)
    stackOutputFilePath = os.path.join(inputPath,newDirName,stackOutputFileName)
    
    # Write Raw Tilt File for IMOD/Etomo
    tiltOutputFile = open(tiltOutputFilePath,'w')
    tiltOutputFile.write("\n".join([str(a) for a in uniqueAngles]))
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