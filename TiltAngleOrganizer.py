## Preamble
"""
# Program: TiltAngleOrganizer.py
# Version: 0.1.0
# Author: Jonathan Myers
# Date Created: Mon Aug 23 16:53:57 2021
# Date Modified: Dec 10 2021
# Purpose: Builds angle sorted image stack of form .st from .mrc images of 
tomography samples for IMOD tomogram reconstruction.
# Imports: sys, re (regular expression), os (operating system), and subprocess.
# Inputs/Arguments: Non-optional global .mrc image data directory path. 
Optional IMOD/Etomo start boolean for completed stack.
# Outputs/Returns: Angle sorted stack (.st) in Tomo sub-directory located in
image data directory. Sorted angle .rawtlt file, dose sorted angles in 
.raworder file, and sorted data intermediate file.
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
    inputPath = "/home/jmyers/Documents/testFolder/NonUnique"
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
    for file in dataFiles:
        dataInfo.append(patternFinder.findall(file)[0])

    # Extract All Image Dates
    allDates = []
    for fileInfo in dataInfo:
        allDates.append(dt.datetime.strptime(fileInfo[timeLocation],parseFormat))
    
    # Determine Efficient Angle Sorting Routine
    allAngles = [float(val[angleLocation]) for val in dataInfo]
    uniqueAngles = sorted(set(allAngles))
    angleNum = len(uniqueAngles)
    
    # Run Efficient Sorting Routine
    if dataLen == angleNum:
        # Sort Files by Angle Without Latest Image Recording
        angleSortedAngleIndex = sorted(range(dataLen),key=lambda x:allAngles[x])
    else:
        # Sort Files by Angle Using Latest Image Recording
        angleSortedAngleIndex = []
        for uniqueAngle in uniqueAngles:
            angleIndices = [index for index,angle in enumerate(allAngles) if angle == uniqueAngle]
            angleDates = [allDates[index] for index in angleIndices]
            angleSortedAngleIndex.append(allDates.index(max(angleDates)))
    angleSortedFiles = [dataFiles[index] for index in angleSortedAngleIndex]
    
    # Sort Angles by Earliest Image Recording
    uniqueDates = [allDates[index] for index in angleSortedAngleIndex]
    doseSortedAngleIndex = sorted(range(angleNum),key=lambda x:uniqueDates[x])
    doseSortedAngles = [uniqueAngles[index] for index in doseSortedAngleIndex]
    
    # Define Output Variables
    # Selects Information from First File
    if dataInfo[0][baseLocation] == "":
        base = "Data"
    else:
        base = dataInfo[0][baseLocation]
    navID = dataInfo[0][navIDLocation]
    
    imodInputFileName = f"{base}_{navID}.txt"
    tiltOutputFileName = f"tilt{navID}.rawtlt"
    orderOutputFileName = f"tilt{navID}.raworder"
    stackOutputFileName = f"tilt{navID}.st"
    
    imodInputFilePath = os.path.join(inputPath,newDirName,imodInputFileName)
    tiltOutputFilePath = os.path.join(inputPath,newDirName,tiltOutputFileName)
    orderOutputFilePath = os.path.join(inputPath,newDirName,orderOutputFileName)
    stackOutputFilePath = os.path.join(inputPath,newDirName,stackOutputFileName)
    
    # Write Raw Tilt File for IMOD/Etomo
    tiltOutputFile = open(tiltOutputFilePath,'w')
    tiltOutputFile.write("\n".join([str(a) for a in uniqueAngles]))
    tiltOutputFile.close()
    
    # Write Order File for emClarity
    orderOutputFile = open(orderOutputFilePath,'w')
    orderOutputFile.write("\n".join([str(a) for a in doseSortedAngles]))
    orderOutputFile.close()
    
    # Write To Text File For IMOD
    imodInputFile = open(imodInputFilePath,'w')
    imodInputFile.write(str(angleNum))
    imodInputFile.write("\n")
    for file in angleSortedFiles:
        imodInputFile.write(file)
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