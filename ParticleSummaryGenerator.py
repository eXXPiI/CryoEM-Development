## Preamble
"""
# Program: ParticleSummaryGenerator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Mar 10 13:23:58 2022
# Date Modified: Mar 10 2022
# Purpose: Generate particle summary in IMOD/PEET format from emClarity PEET
motive list analog. This script can also be adjusted to work with PEET motive
lists directly. The particle proection from IMOD clonemodel is also run if the
particle model file is present.
# Imports: sys, os (operating system), numpy, subprocess
# Inputs/Arguments: Non-optional global .csv particle data directory file path.
Non-optional binning factor.
# Outputs/Returns: Euler and slicer angle files, particle summary, and 
particle projection if model exists; all in parent directory.
"""

## Articles

def ParticleSummaryGenerator(inputPath,binSelect):
    import os
    import numpy as np
    import subprocess as sp
    
    # Move To Relevant Directory
    os.chdir(os.path.dirname(inputPath))
    
    # Import Particle Motive List Analog
    inputData = np.loadtxt(inputPath,delimiter=',')
    dataLen = np.size(inputData,axis=0)
    
    # Extract Particle Coordinates (PEET And emClarity -> (10,11,12))
    coordinateColumns = (10,11,12)
    coordinatesLen = len(coordinateColumns)
    coordinates = inputData[:,coordinateColumns]
    coordinatesBin = np.zeros([dataLen,coordinatesLen])
    
    # Extract Particle Euler Angles (PEET -> (16,17,18) And emClarity ->(13,14,15))
    eulerColumns = (13,14,15)
    #eulerLen = len(eulerColumns)
    eulerAngles = inputData[:,eulerColumns]
    
    # Mutate Particle Coordinates By Bin Value
    for particle in range(dataLen):
        for column in range(coordinatesLen):
            coordinatesBin[particle,column] = coordinates[particle,column]/binSelect
    
    # Prepare Euler Angles File For PEET MOTL2Slicer Script
    eulerFileName = "EulerAngles.csv"
    slicerFileName = "SlicerAngles.csv"
    eulerFormatter = ['%.6f','%.6f','%.6f']
    np.savetxt(eulerFileName,eulerAngles,fmt=eulerFormatter,delimiter=',')
    
    # Run PEET MOTL2Slicer Script
    # When debugging, sp.run will return an "ENOTTY" error that is suspected 
    # to come from the calling of a command that reports time. This error does 
    # not seem to influence the performance of the script nor the resulting 
    # outputs. Behavior not seen when run from CLI.
    slicerCommand = " ".join(["MOTL2Slicer",eulerFileName,slicerFileName])
    sp.run(slicerCommand,shell=True)
    
    # Read And Mutate Slicer Angles (X,Y,Z)->(-X,Y,Z)
    slicerAngles = np.loadtxt(slicerFileName,delimiter=',')
    for xAngle in range(dataLen):
        slicerAngles[xAngle,0] = -slicerAngles[xAngle,0]
    
    # Build Particle Summary
    summary = np.ones([dataLen,7])
    summary[:,(1,2,3)] = coordinatesBin
    summary[:,(4,5,6)] = slicerAngles
    
    # Generate Particle Summary File
    summaryFileName = "ParticleSummary.csv"
    info = "#contour,X,Y,Z,xAngle,yAngle,zAngle"
    reduce = ['%.0f','%.6f','%.6f','%.6f','%.6f','%.6f','%.6f']
    np.savetxt(summaryFileName,summary,fmt=reduce,delimiter=',',header=info,comments='')
    
    # If Particle Model Exists Run IMOD clonemodel To Build Particle Projection
    particleFileName = "Particle.mod"
    projectionFileName = "ParticleProjection.mod"
    if os.path.isfile(particleFileName):
        # Run IMOD clonemodel
        cloneCommand = " ".join(["clonemodel","-at",summaryFileName,
                                 particleFileName,projectionFileName])
        sp.run(cloneCommand,shell=True)
    else:
        print("Particle Summary Generated But IMOD clonemodel Not Run")


# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    
    # Testing/Debugging Lines
    """
    inputPath = "/home/jmyers/Documents/testFolder/ParticleSummary/tilt70_1_bin6.csv"
    binSelect = 6
    """
    
    # Define Input Variables
    inputPath = str(sys.argv[1])
    binSelect = int(sys.argv[2])

    # Main Script Run
    ParticleSummaryGenerator(inputPath,binSelect)

# M02 End Program