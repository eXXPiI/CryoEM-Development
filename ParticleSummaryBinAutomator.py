## Preamble
"""
# Program: ParticleSummaryBinAutomator.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Mar  3 15:29:15 2022
# Date Modified: Mar 7 2022
# Purpose: Generate Binned particle sumamry file for IMOD visualization.
# Imports: 
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles

def ParticleSummaryBinAutomator(inputPath,outoutPath,binSelect):
    import numpy as np
    
    # Import Summary File
    inputData = np.loadtxt(inputPath,delimiter=',',skiprows=1)
    dataLen = np.size(inputData,axis=0)
    
    # Mutate Coordinates (x,y,z)->(1,2,3) By Bin Value
    for particle in range(dataLen):
        for column in (1,2,3):
            inputData[particle,column] = inputData[particle,column]/binSelect
    
    # Generate New Binned Summary File
    info = "#contour,X,Y,Z,xAngle,yAngle,zAngle"
    reduce = ['%.0f','%.6f','%.6f','%.6f','%.6f','%.6f','%.6f']
    #reduce = ['%.0f + %dj','%f + %dj','%f + %dj','%f + %dj','%f + %dj','%f + %dj','%f + %dj']
    np.savetxt(outputPath,inputData,fmt=reduce,delimiter=',',header=info,comments='')
    
    
# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    
    # Define Input Variables
    inputPath = "/home/jmyers/Documents/FHV_Crown/Structure/N49_Segmentation/ParticleSummary.csv"
    outputPath = "/home/jmyers/Documents/FHV_Crown/Structure/N49_Segmentation/ParticleSummary-bin3.csv"
    binSelect = 3

    # Main Script Run
    ParticleSummaryBinAutomator(inputPath,outputPath,binSelect)

# M02 End Program