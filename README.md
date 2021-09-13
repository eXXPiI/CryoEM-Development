# CryoEM-Development
CryoEM image processing software development repository.

## TiltAngleOrganizer Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python TiltAngleOrganizer.py <Path/To/Data> [1 or 0]." Here, the data path must end in a directory that contains ONLY a tilt series of MRC files. The optional input determines if the resulting organized MRC file based stack is opened in 3dmod. Without an optional argument, 3dmond is not opened. This script builds a sub-directory called "Tomo" where output files are generated.

## BinVolumeAutomator ScriptiltAngleOrganizer
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python BinVolumeAutomator.py <Path/To/Data> [Integer]." Here the data path must end in a directory that contains the target tomogram reconstructions for binning. Other files may be present as they are automatically sorted out from the reconstructions based on the naming scheme from IMOD. The optional argument determines the uniform 3D binning parameter (e.g. 1 ==> 1X1X1 and 2 ==> 2X2X2). If the optional argument is not provided, the program defaults to a binning of 2 which reduces the image size by a factor of 8.
