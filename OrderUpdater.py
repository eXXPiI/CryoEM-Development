## Preamble
"""
# Program: OrderUpdater.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Dec  9 15:04:48 2021
# Date Modified: Dec 10 2021
# Purpose: Generate true recorded angle .order file for later emClarity
processing. Code can run without shell call.
# Imports: sys, os (operating system)
# Inputs/Arguments: Requires main image dataset directory path.
# Outputs/Returns: Generates .order file in relevant Tomo subdirectory.
"""

## Articles

def OrderUpdater(inputPath):
    import os
    
    # Acquire Subdirectories From Directory
    dataDirectory = os.chdir(inputPath)
    dataPartitions = os.listdir(dataDirectory)
    imageLen = len(dataPartitions)
    
    # Acquire Relevant Files From Within Image Data Partitions
    idealAngleFileName =  lambda navID: f"{navID}/Tomo/tilt{navID}.rawtlt"
    actualAngleFileName = lambda navID: f"{navID}/Tomo/tilt{navID}.tlt"
    oldOrderFileName = lambda navID: f"{navID}/Tomo/tilt{navID}.raworder"
    newOrderFileName = lambda navID: f"{navID}/Tomo/tilt{navID}.order"
    
    # Generate Data Lists For Relevant Files
    # images => [[.rawtlt, .tlt, .order],...]
    # images => [[Ideal Angles, Actual Angles, Order Angles],...]
    images = []
    for partition in dataPartitions:
        # files => [Ideal Angles, Actual Angles, Order Angles]
        files = []
        
        idealAngleFile = open(idealAngleFileName(partition),'r')
        idealAngles = [float(a) for a in idealAngleFile.readlines()]
        idealAngleFile.close()
        files.append(idealAngles)
        
        actualAngleFile = open(actualAngleFileName(partition),'r')
        actualAngles = [float(a) for a in actualAngleFile.readlines()]
        actualAngleFile.close()
        files.append(actualAngles)
        
        orderFile = open(oldOrderFileName(partition),'r')
        orderAngles = [float(a) for a in orderFile.readlines()]
        orderFile.close() 
        files.append(orderAngles)
        
        images.append(files)
    
    # Iterate Through Images And Read Data
    imageOrder = []
    for image in images:
        actualOrderAngles = []
        doseOrderAngleError = []
        # Loop According To Order File Angles
        for idealAngle in image[2]:
            idealAngleIndex = image[0].index(idealAngle)
            actualAngle = image[1][idealAngleIndex]
            actualOrderAngles.append(actualAngle)
            doseOrderAngleError.append(round(abs(actualAngle)-abs(idealAngle),3))
        imageOrder.append(actualOrderAngles)
    
    # Write Over Order Files
    for index in range(imageLen):
        partition = dataPartitions[index]
        doseOrderAngles = imageOrder[index]
        orderFile = open(newOrderFileName(partition),'w')
        orderFile.write("\n".join([str(a) for a in doseOrderAngles]))
        orderFile.close()

    
# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    # Define Input Variables
    inputPath = str(sys.argv[1])
    #inputPath = "/home/jmyers/Documents/testFolder/NavID_Group"
    OrderUpdater(inputPath)

# M02 End Program