# Script to delete unannotated images to cleanup data for YoloV4

import os
import glob
import argparse
from tqdm import tqdm

def delete_unannotated_images(inputDirectory):
    """
    Function to delete unannotated images to cleanup data for YoloV4.

    Parameters
    ----------
    inputDirectory  : str
                      Path to the input directory containing image and annotation files

    Returns
    -------
    None
    """
    print("Deleting Unannotated Images...")
    unannotatedImageCount = 0

    for individualImagePath in tqdm(glob.glob(inputDirectory + "\\*.jpg")):
        imageName = os.path.splitext(individualImagePath)[0]
        labelName = imageName + ".txt"

        if (os.path.isfile(labelName) == False):
            unannotatedImageCount += 1
            os.remove(imageName + ".jpg")

    print("Unannotated Images Deleted Successfully!! (Total Count: {})".format(unannotatedImageCount))


def data_cleanup(inputDirectory):
    """
    Wrapper function to pass the arguments to the delete_unannotated_images function.

    Parameters
    ----------
    inputDirectory  : str
                      Path to the input directory containing image and annotation files

    Returns
    -------
    None
    """
    delete_unannotated_images(inputDirectory)

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
    parser = argparse.ArgumentParser(description="Script to delete unannotated images to cleanup data for YoloV4")
    parser.add_argument("-i", "--inputDirectory", type=str, required=True, help="Path to the input directory containing image and annotation files")
    args = parser.parse_args()

    data_cleanup(args.inputDirectory)


if __name__ == '__main__':
    main()