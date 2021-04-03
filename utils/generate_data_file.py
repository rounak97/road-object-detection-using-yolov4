# Script to generate data file containing relative paths to the training, validation and backup folders for YOLOv4

import os
import argparse

def create_data_file(classes, trainingPath, validationPath, names, backup, outputPath):
    """
    Function to generate data file containing relative paths to the training, validation and backup folders for YOLOv4.

    Parameters
    ----------
    classes         : int
                      Total number of classes
    trainingPath    : str
                      Path to the training folder (Relative to darknet)
    validationPath  : str
                      Path to the validation folder (Relative to darknet)
    names           : str
                      Path to the names file (Relative to darknet)
    backup          : str
                      Path to the backup folder (Relative to darknet)
    outputPath      : str
                      Full path to the output folder

    Returns
    -------
    None
    """    
    print("Generating data files for YOLOv4...")

    outputPath = os.path.normpath(outputPath)
    fileName = os.path.basename(os.path.normpath(names)).split(".")[0] + ".data"
    overallPath = os.path.join(outputPath, fileName)
    print("overallPath = ", overallPath)

    with open(overallPath, "w+") as outputFile:
        outputFile.write(("classes = " + repr(classes) + "\n").replace('"','').replace("'",""))
        outputFile.write(("train = " + repr(os.path.normpath(trainingPath)) + "\n").replace('"','').replace("'",""))
        outputFile.write(("valid = " + repr(os.path.normpath(validationPath)) + "\n").replace('"','').replace("'",""))
        outputFile.write(("names = " + repr(os.path.normpath(names)) + "\n").replace('"','').replace("'",""))
        outputFile.write(("backup = " + repr(os.path.normpath(backup)) + "\n").replace('"','').replace("'",""))

    print("Data file generation successful!")

def generate_data_file(classes, trainingPath, validationPath, names, backup, outputPath):
    """
    Wrapper function to pass the arguments to the create_data_files() function.

    Parameters
    ----------
    classes         : int
                      Total number of classes
    trainingPath    : str
                      Path to the training folder (Relative to darknet)
    validationPath  : str
                      Path to the validation folder (Relative to darknet)
    names           : str
                      Path to the names file (Relative to darknet)
    backup          : str
                      Path to the backup folder (Relative to darknet)
    outputPath      : str
                      Full path to the output folder

    Returns
    -------
    None
    """
    create_data_file(classes, trainingPath, validationPath, names, backup, outputPath)

def main():
    """
    Entry point for the scripts.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(description="Script to generate data file containing relative paths to the training, validation and backup folders for YOLOv4")
    parser.add_argument("-c", "--classes", type=int, required=True, help="Total number of classes")
    parser.add_argument("-t", "--train", type=str, required=True, help="Path to the training folder (Relative to darknet)")
    parser.add_argument("-v", "--validation", type=str, required=True, help="Path to the validation folder (Relative to darknet)")
    parser.add_argument("-n", "--names", type=str, required=True, help="Path to the names file (Relative to darknet)")
    parser.add_argument("-b", "--backup", type=str, required=True, help="Path to the backup folder (Relative to darknet)")
    parser.add_argument("-o", "--output", type=str, required=True, help="Full path to the output folder")
    args = parser.parse_args()

    generate_data_file(args.classes, args.train, args.validation, args.names, args.backup, args.output)

if __name__ == "__main__":
    main()
