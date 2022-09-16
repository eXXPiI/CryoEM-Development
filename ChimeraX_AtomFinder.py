## Preamble
"""
# Program: ChimeraX_AtomFinder.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Fri Aug  5 13:45:53 2022
# Date Modified: Aug 8 2022
# Purpose: 
# Imports: 
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles

from chimerax.atomic import all_atomic_structures
import numpy as np

# Import Structures And Get Atoms And Coordinates
structures = all_atomic_structures(session)
atoms = structures[0].atoms
coords = atoms.scene_coords

# Find Alpha Carbons
RTracker = []
for i in range (len(atoms)):
    residue = str(atoms[i]).split()
    if residue[3] == "CA":
        # (Residue Number,Index Number)
        tracker = (int(residue[2]),i)
        RTracker.append(tracker)
RArray = np.array(RTracker)

# Save Data Files
np.savetxt('/home/jmyers/Documents/FHV_Crown/Structure/PISA/AtomCoordinates.csv',coords,delimiter=',')
np.savetxt('/home/jmyers/Documents/FHV_Crown/Structure/PISA/AlphaCarbonMeta.csv',RArray,fmt='%i',delimiter=',')

# Code Executed
print("Code Executed")

# M02 End Program