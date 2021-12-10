## Preamble
"""
# Program: OrderUpdater.py
# Version: 0.0.1
# Author: Jonathan Myers
# Date Created: Thu Dec  9 15:04:48 2021
# Date Modified: Dec 9 2021
# Purpose: 
# Imports: 
# Inputs/Arguments: 
# Outputs/Returns: 
"""

## Articles

def OrderUpdater(inputPath):
    import os
    import subprocess as sp
    
    # Acquire Subdirectories From Directory
    dataDirectory = os.chdir(inputPath)
    dataPartitions = os.listdir(dataDirectory)

    
# If Code Independent, Run; If Code Imported, Do Not Run
if __name__ == '__main__':
    import sys
    # Define Input Variables
    #inputPath = str(sys.argv[1])
    inputPath = "/home/jmyers/Documents/testFolder/Unique"
    OrderUpdater(inputPath)

# M02 End Program