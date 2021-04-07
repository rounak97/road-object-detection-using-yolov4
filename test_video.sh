#!/bin/bash

#####################################################################################################################
######################################## UPDATE BELOW PATHS BEFORE RUNNING ##########################################
#####################################################################################################################

# Provide full path to the darknet repository
DARKNET_REPO_PATH=/home/sourab/Data/temp3/darknet                              #e.g. /home/user/darknet

# Provide full paths to the road-object-detection-using-yolo-v4 repository
ROAD_REPO_PATH=/home/sourab/Data/temp3/road-object-detection-using-yolov4      #e.g. /home/user/repo-name

# Provide full path to the script folder
SCRIPT_FOLDER=/home/sourab/Data/repos/road-object-detection-using-yolov4       #e.g. /home/user/master-thesis/scripts

# Provide full path to the input image
INPUT=$DARKNET_REPO_PATH/data/bdd100k/images/100k/test/cc1c40bb-d0ce34c5.jpg   #e.g. /home/user/image.jpg

# Provide file name of the output file
OUT_FILENAME=cc1c40bb-d0ce34c5-output                                          #e.g. cc1c40bb-d0ce34c5-output

# Provide full path to the weights file
WEIGHTS=$ROAD_REPO_PATH/weights/yolov4-tiny-bdd100k_best.weights               #e.g. /home/user/darknet/backup/

# Provide full path to the config file
CONFIG_FILE=$DARKNET_REPO_PATH/cfg/yolov4-tiny-bdd100k.cfg                     #e.g. /home/user/darknet/cfg/

# Provide full path to the data file
DATA_FILE=$DARKNET_REPO_PATH/data/bdd100k/bdd100k.data                         #e.g. /home/user/darknet/data/

#####################################################################################################################
######################################## UPDATE BELOW FLAGS BEFORE RUNNING ##########################################
#####################################################################################################################

# Set to True if windows inference display is **not** available
DONT_SHOW=False                                                                #e.g. True, False

# Set to True if bounding box coordinates of the detected objects need to be displayed
EXT_OUTPUT=True                                                                #e.g. True, False

# Set a value to remove detections with lower confidence
THRESH=0.25                                                                    #e.g. 0.1, 0.2, 0.3...

#####################################################################################################################
######################################## DO NOT MODIFY THE SETTINGS BELOW ###########################################
#####################################################################################################################

# Print current path and provided path
echo "Printing paths and flags set..."
echo "Path to the darknet repository: $DARKNET_REPO_PATH"
echo "Path to the road-object-detection-using-yolov4 repository: $ROAD_REPO_PATH"
echo "Path of the bash script: $SCRIPT_FOLDER"
echo "Path to the input image: $INPUT"
echo "Value of output file name: $OUT_FILENAME"
echo "Path to the weights file: $WEIGHTS"
echo "Path to the config file: $CONFIG_FILE"
echo "Path to the data file: $DATA_FILE"
echo "Value of dont show flag: $DONT_SHOW"
echo "Value of external output: $EXT_OUTPUT"
echo "Value of confidence threshold: $THRESH"
echo ""

# Activate conda virtual environment to run from bash
echo "Activating conda virtual environment to run from bash..."
echo ""
conda init bash

# Activating the conda virtual environment
echo "Creating the conda virtual environment..."
echo ""
conda activate yolo

# Test image
python $DARKNET_REPO_PATH/darknet_video.py --input $INPUT --out_filename $OUT_FILENAME --weights $WEIGHTS \
--dont_show $DONT_SHOW --ext_output $EXT_OUTPUT --config_file $CONFIG_FILE  --data_file $DATA_FILE \
--thresh $THRESH

# Deactivate Conda Environment
echo "Deactivating Conda Environment..."
echo ""
conda deactivate

# Exit script
echo "Exiting script..."
echo ""
return 0
