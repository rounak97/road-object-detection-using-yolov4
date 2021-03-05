# Script to generate text files containing training and validation image paths for YoloV4

import os
import glob
import argparse
from tqdm import tqdm

def create_text_files(inputTrainingDirectory, inputValidationDirectory, outputDirectory):
    """
    Function to generate text files containing training and validation image paths for YoloV4.

    Parameters
    ----------
    inputTrainingDirectory      : str
                                  Path to the input directory containing training image and annotation files
    inputValidationDirectory    : str
                                  Path to the input directory containing validation image and annotation files
    outputDirectory             : str
                                  Path to the output directory

    Returns
    -------
    None
    """
    
    print("Generating Text Files for Training Data...")

    with open(outputDirectory + "\\Train.txt", "w+") as trainingOutputFile:
        
        for individualTrainingImagePath in tqdm(glob.glob(inputTrainingDirectory + "\\*.jpg")):
            trainingOutputFile.write(repr(individualTrainingImagePath) + "\n")

    print("Files Generated for Training Data Successfully!!")

    print("\n\n")

    print("Generating Text Files for Validation Data...")

    with open(outputDirectory + "\\Val.txt", "w+") as validationOutputFile:
        
        for individualValidationImagePath in tqdm(glob.glob(inputValidationDirectory + "\\*.jpg")):
            validationOutputFile.write(repr(individualValidationImagePath) + "\n")

    print("Files Generated for Validation Data Successfully!!")


def generate_paths(inputTrainingDirectory, inputValidationDirectory, outputDirectory):
    """
    Wrapper function to pass the arguments to the create_text_files function.

    Parameters
    ----------
    inputTrainingDirectory      : str
                                  Path to the input directory containing training image and annotation files
    inputValidationDirectory    : str
                                  Path to the input directory containing validation image and annotation files
    outputDirectory             : str
                                  Path to the output directory

    Returns
    -------
    None
    """
    create_text_files(inputTrainingDirectory, inputValidationDirectory, outputDirectory)

def main():
    """
    Entry point for the script.

    Parameters
    ----------
    None

    Returns
    -------
    None
    """
    parser = argparse.ArgumentParser(description="Script to generate text files containing training and validation image paths for YoloV4")
    parser.add_argument("-it", "--inputTrainingDirectory", type=str, required=True, help="Path to the input directory containing training image and annotation files")
    parser.add_argument("-iv", "--inputValidationDirectory", type=str, required=True, help="Path to the input directory containing validation image and annotation files")
    parser.add_argument("-o", "--outputDirectory", type=str, required=True, help="Path to the output directory")
    args = parser.parse_args()

    generate_paths(args.inputTrainingDirectory, args.inputValidationDirectory, args.outputDirectory)


if __name__ == '__main__':
    main()