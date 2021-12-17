# CryoEM-Development
CryoEM image processing software development repository.

## TiltAngleOrganizer Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python TiltAngleOrganizer.py <Global/Path/To/Data> [1 or 0]." Here, the data path must end in a directory that contains ONLY a tilt series of MRC files. Multiple images of the same angle are okay as the script will search for and use the latest recorded image. Images must be named according to the SerialEM naming scheme. PNCC naming conventions are also valid. An example is "Base_GridNum_NavID_ImageNum_Angle_Date_Time.Extension" where Base, GridNum, and ImageNum are all optional. The optional input determines if the resulting organized MRC file based stack is opened in 3dmod. Without an optional argument, 3dmond is not opened. This script builds a sub-directory called "Tomo" where output files are generated.

## BinVolumeAutomator Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python BinVolumeAutomator.py <Global/Path/To/Data> [Integer]." Here, the data path must end in a directory that contains the target tomogram reconstructions for binning. Other files may be present as they are automatically sorted out from the reconstructions based on the naming scheme from IMOD. The optional argument determines the uniform 3D binning parameter (e.g. 1 ==> 1X1X1 and 2 ==> 2X2X2). If the optional argument is not provided, the program defaults to a binning of 2 which reduces the image size by a factor of 8.

## RotateAutomator Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python RotateAutomator.py <Global/Path/To/Data> [Float]." Here, the data path must end in a directory that contains partitioned target image stacks for rotation that are consistent with the structure as generated by the TiltAngleOrganizer Script (e.g. <DatasetHome/NavID/Tomo/tiltNavID.st>). Other files may be present as they are ignored based on the naming scheme consistent with emClarity. The optional argument determines the rotation angle in degrees that are consistent with the crossproduct (i.e. (+) ==> CCW and (-) ==> CW). If the optional argument is not provided, the program defaults to a rotation of 90 degrees.

## OrderUpdater Script
This script is intended to be used in a CLI. Navigate to the directory containing this file and open a terminal there. Then type "python OrderUpdater.py <Global/Path/To/Data> [Float]." Here, the data path must end in a directory that contains partitioned target image stacks for rotation that are consistent with the structure as generated by the TiltAngleOrganizer Script (e.g. <DatasetHome/NavID/Tomo/tiltNavID.st>). Other files may be present as they are ignored based on the naming scheme consistent with emClarity. This script then generates an .order file with the actual tomography angles for later use in emClarity image processing.