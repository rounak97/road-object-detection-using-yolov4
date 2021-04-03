# Script to convert Berkely Deep Drive Annotations from JSON file to YoloV4 Compatible Text File for Transfer Learning

import json
import argparse
from tqdm import tqdm

def json_to_text(inputData, namesData, outputDirectory, maxWidth, maxHeight):
    """
    Function to convert Berkely Deep Drive Annotations from JSON file to YoloV4 Compatible Text File.

    The format of Berkely Deep Drive Annotations from JSON file is as follows:
    Scalabel Format (Link: https://doc.scalabel.ai/format.html)

    The format of YoloV4 Compatible Text File is as follows:
    <class> <x> <y> <width> <height>

    Parameters
    ----------
    inputData       : dict
                      Input data from the JSON file
    namesData       : list
                      Input data from the NAMES file
    outputDirectory : str
                      Path to output directory
    maxWidth        : int
                      Maximum width of the image
    maxHeight       : int
                      Maximum height of the image

    Returns
    -------
    None
    """

    print("Converting JSON Files to Text Files...")

    for individualImage in tqdm(inputData):
        imageName = individualImage["name"]
        outputFilePath = outputDirectory + imageName[:-4]+ ".txt"

        with open(outputFilePath, "w+") as outputFile:

            for label in individualImage["labels"]:
                
                if "box2d" not in label:
                    continue

                cooridnates = label["box2d"]

                W = (cooridnates["x2"] - cooridnates["x1"])/maxWidth
                H = (cooridnates["y2"] - cooridnates["y1"])/maxHeight

                MX = ((cooridnates["x1"] + cooridnates["x2"])/2)/maxWidth
                MY = ((cooridnates["y1"] + cooridnates["y2"])/2)/maxHeight
                
                if (label["category"] in namesData):
                    classValue = namesData.index(label["category"])
                else:
                    classValue = -1

                outputFile.write(repr(classValue) + " " + repr(MX) + " " + repr(MY) + " " + repr(W) + " " + repr(H) + "\n")

    print("Conversion Succesful!!")


def convert_labels(inputJsonPath, inputNamesPath, outputDirectory, maxWidth, maxHeight):
    """
    Wrapper function to pass the arguments to the json_to_text() function.

    Parameters
    ----------
    inputJsonPath   : str
                      Input path to the JSON file
    inputNamesPath  : str
                      Input path to the NAMES file
    outputDirectory : str
                      Path to output directory
    maxWidth        : int
                      Maximum width of the image
    maxHeight       : int
                      Maximum height of the image

    Returns
    -------
    None
    """
    jsonData = json.load(open(inputJsonPath, "r"))
    namesData = [classValue.rstrip("\n") for classValue in open(inputNamesPath, "r")]
    
    json_to_text(jsonData, namesData, outputDirectory, maxWidth, maxHeight)


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
    parser = argparse.ArgumentParser(description="Script to convert Berkely Deep Drive Annotations from JSON file to YoloV4 Compatible Text File for Transfer Learning")
    parser.add_argument("-ij", "--inputJsonPath", type=str, required=True, help="Path to the input JSON File")
    parser.add_argument("-in", "--inputNamesPath", type=str, required=True, help="Path to the input NAMES File")
    parser.add_argument("-o", "--outputDirectory", type=str, required=True, help="Path to the output directory")
    parser.add_argument("-mw", "--maxWidth", type=int, default=1280, help="Max width of the image")
    parser.add_argument("-mh", "--maxHeight", type=int, default=720, help="Max height of the image")
    args = parser.parse_args()

    convert_labels(args.inputJsonPath, args.inputNamesPath, args.outputDirectory, args.maxWidth, args.maxHeight)


if __name__ == '__main__':
    main()