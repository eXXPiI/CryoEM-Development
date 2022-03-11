# CryoEM-Development
CryoEM image processing software development repository.

## Script Usage
Many of the scripts developed within this repository are intended to both speed up and improve the consistency of the processing of tomography datasets.
Some of the scripts are also intended to function as intermediates between emClarity and IMOD processing workflows.
IMOD (recent but unspecified), PEET (v1.15.x or later), and emClarity (recent but unspecified) are all required to be installed on the machine running these scripts.
Python 3 (3.8.8 Anaconda used by author) is also assumed to be installed and working with numpy.

### TiltAngleOrganizer Script
This script is intended to be used in a CLI. 
Navigate to the directory containing this file and open a terminal there. 
Then type "python TiltAngleOrganizer.py <Global/Path/To/Data> [1 or 0]." 
Here, the data path must end in a directory that contains ONLY a tilt series of MRC files. 
Multiple images of the same angle are okay as the script will search for and use the latest recorded image. 
Images must be named according to the SerialEM naming scheme. PNCC naming conventions are also valid. 
An example is "Base_GridNum_NavID_ImageNum_Angle_Date_Time.Extension" where Base, GridNum, and ImageNum are all optional. 
The optional input determines if the resulting organized MRC file based stack is opened in 3dmod. 
Without an optional argument, 3dmond is not opened. 
This script builds a sub-directory called "Tomo" where output files are generated.

### BinVolumeAutomator Script
This script is intended to be used in a CLI. 
Navigate to the directory containing this file and open a terminal there. 
Then type "python BinVolumeAutomator.py <Global/Path/To/Data> [Integer]." 
Here, the data path must end in a directory that contains the target tomogram reconstructions for binning. 
Other files may be present as they are automatically sorted out from the reconstructions based on the naming scheme from IMOD. 
The optional argument determines the uniform 3D binning parameter (e.g. 1 ==> 1X1X1 and 2 ==> 2X2X2). 
If the optional argument is not provided, the program defaults to a binning of 2 which reduces the image size by a factor of 8.

### RotateAutomator Script
This script is intended to be used in a CLI. 
Navigate to the directory containing this file and open a terminal there. 
Then type "python RotateAutomator.py <Global/Path/To/Data> [Float]." 
Here, the data path must end in a directory that contains partitioned target image stacks for rotation that are consistent with the structure as generated by the TiltAngleOrganizer Script (e.g. <DatasetHome/NavID/Tomo/tiltNavID.st>). 
Other files may be present as they are ignored based on the naming scheme consistent with emClarity. 
The optional argument determines the rotation angle in degrees that are consistent with the crossproduct (i.e. (+) ==> CCW and (-) ==> CW). 
If the optional argument is not provided, the program defaults to a rotation of 90 degrees.

### OrderUpdater Script
This script is intended to be used in a CLI. 
Navigate to the directory containing this file and open a terminal there. 
Then type "python OrderUpdater.py <Global/Path/To/Data>." 
Here, the data path must end in a directory that contains partitioned target image stacks for rotation that are consistent with the structure as generated by the TiltAngleOrganizer Script (e.g. <DatasetHome/NavID/Tomo/tiltNavID.st>). 
Other files may be present as they are ignored based on the naming scheme consistent with emClarity. 
This script then generates an .order file with the actual tomography angles for later use in emClarity image processing.

### FSCPlotter Script
This script is intended to be used in a CLI.
Navigate to the directory containing this file and open a terminal there.
Then type "python FSCPlotter.py <Global/Path/To/Data> <format>" where the format is generally either "png" or "pdf."
Here, the data path must end in a directory that contains the target FSC data file that is generated by emClarity (*_fsc_GLD.txt).
That file is read and others are ignored to produce a plot of the FSC curve.
The file is universally modular with the first column consisting of the spatial frequency components and the second column representing the FSC value.
Any additional columns are ignored but can easily be implemented into additional code.
An output file is generated and saved into the data directory.

### ParticleSummaryGenerator Script
This script is intended to be used in a CLI.
Navigate to the directory containing this file and open a terminal there.
Then type "python ParticleSummaryGenerator.py <Global/Path/To/Data> Integer."
Here, that data path must end in a directory that contains the target particle motive list analog from emClarity.
That file is, by default, anticipated to be called "Particle.csv" but can be of another name.
That file may be extracted from the convmap directory or from the MAT metadata file.
Other files can be present, but they must not be CSV files if there is not a specific "Particle.csv" within the directory.
If there is a CSV file present without being named "Particle.csv" it will be used as the input data.
The output files, including CSV files, of the script are ignored and can be present even if there is no specifically named "Particle.csv."
The other non-optional argument is the binning of the visualization tomogram.
If a "Particle.mod" file is present, the IMOD clonemodel script will also be run to generate a final particle projection.
"Particle.mod" must be processed by binning (at the same factor as the visualization tomogram) a reconstruction using the emClarity "rescale" command and then converting to an isosurface within IMOD.

## Code To Be Developed In Future
Some processes are worth developing into automated scripts but others sometimes are not.
These programs may be useful to standardize and speed up the generation of publication-grade graphics.

### Visualize Euler Angles From 3D Polar Plot
Generate polar plot of all particle angles to see angle distribution.
This may be accomplished within cryoSPARC or may be need to be developed.


M02 End Program