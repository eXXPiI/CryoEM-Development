# CryoEM-Development
CryoEM image processing software development repository.

## TiltAngleOrganizer Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python TiltAngleOrganizer.py <Path/To/Data> [1 or 0]." Here, the data path must end in a duirectory that contains ONLY a tilt series of MRC files. The optional input determines if the resulting organized MRC file based stack is opened in 3dmod. Without an optional argument, 3dmond is not opened. This script builds a sub-directory called "Tomo" where output files are generated.
