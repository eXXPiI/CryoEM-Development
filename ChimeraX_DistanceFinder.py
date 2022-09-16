## Preamble
"""
# Program: ChimeraX_DistanceFinder.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Mon Aug  8 15:35:38 2022
# Date Modified: Aug 8 2022
# Purpose: 
# Imports: 
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles

def ComputeDistance(P1,P2):
    #import numpy as np
    dx2 = (P2[0]-P1[0])**2
    dy2 = (P2[1]-P1[1])**2
    dz2 = (P2[2]-P1[2])**2
    distance = sqrt(dx2+dy2+dz2)
    return distance

import os
import numpy as np

# Set Up Directory And Subdirectory
inputPath = "/home/jmyers/Documents/FHV_Crown/Structure/PISA/"
os.chdir(inputPath)
newDirName = "Distances"
#os.mkdir(newDirName)

# Load ChimeraX Generated Data Files
AlphaCarbonMeta = np.loadtxt("AlphaCarbonMeta.csv",dtype=int,delimiter=',')
AtomCoordinates = np.loadtxt("AtomCoordinates.csv",dtype=float,delimiter=',')

# For Multimer, Add Column(s)
subunitDivision = 2
uniqueResidues = int(np.shape(AlphaCarbonMeta)[0]/subunitDivision)
residues = AlphaCarbonMeta[:uniqueResidues,:2]
for i in range(1,subunitDivision):
    lowerLimit = uniqueResidues*i
    upperLimit = uniqueResidues*(i+1)
    indices = np.array(AlphaCarbonMeta[lowerLimit:upperLimit,1])
    #residues = np.append(residues,indices,1)
    residues = np.append(residues,indices,1)
print("DONE")

# Compute Distances And Track
startResidues = []q
endResidues = []

distances = []

for i in startResidues:
    for j in endResidues:
        print("DONE")


# M02 End Program