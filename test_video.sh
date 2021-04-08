#!/bin/bash

#####################################################################################################################
######################################## UPDATE BELOW PATHS BEFORE RUNNING ##########################################
#####################################################################################################################

# Provide full path to the darknet repository
DARKNET_REPO_PATH=/home/sourab/Data/temp5/darknet                              #e.g. /home/user/darknet

# Provide full paths to the road-object-detection-using-yolo-v4 repository
ROAD_REPO_PATH=/home/sourab/Data/temp3/road-object-detection-using-yolov4      #e.g. /home/user/repo-name

# Provide full path to the input video
INPUT=/home/sourab/Data/temp6/test-output.avi                                  #e.g. /home/user/video.avi

# Provide file name of the output file
OUT_FILENAME=/home/sourab/Data/temp6/test-output-yolo.avi                      #e.g. /home/user/video-output.avi

# Provide full path to the weights file
WEIGHTS=$ROAD_REPO_PATH/weights/yolov4-tiny-bdd100k_best.weights               #e.g. /home/user/darknet/backup/

# Provide full path to the config file
CONFIG_FILE=$DARKNET_REPO_PATH/cfg/yolov4-tiny-bdd100k.cfg                     #e.g. /home/user/darknet/cfg/

# Provide full path to the data file
DATA_FILE=$DARKNET_REPO_PATH/data/bdd100k/bdd100k.data                         #e.g. /home/user/darknet/data/

#####################################################################################################################
######################################## UPDATE BELOW FLAGS BEFORE RUNNING ##########################################
#####################################################################################################################

# Set a value to remove detections with lower confidence
THRESH=0.25                                                                    #e.g. 0.1, 0.2, 0.3...

#####################################################################################################################
######################################## DO NOT MODIFY THE SETTINGS BELOW ###########################################
#####################################################################################################################

# Print current path and provided path
echo "Printing paths and flags set..."
echo "Path to the darknet repository: $DARKNET_REPO_PATH"
echo "Path to the road-object-detection-using-yolov4 repository: $ROAD_REPO_PATH"
echo "Path to the input image: $INPUT"
echo "Value of output file name: $OUT_FILENAME"
echo "Path to the weights file: $WEIGHTS"
echo "Path to the config file: $CONFIG_FILE"
echo "Path to the data file: $DATA_FILE"
echo "Value of confidence threshold: $THRESH"
echo ""

# Initialize conda virtual environment to run from bash
echo "Activating conda virtual environment to run from bash..."
echo ""
conda init bash && echo "Conda virtual environment initialized successfully!"

# Activating the conda virtual environment
echo "Activating the conda virtual environment..."
echo ""
source ~/Data/miniconda3/etc/profile.d/conda.sh                # Workaround (conda activate does not work from bash)
conda activate yolo && echo "Conda virtual environment activated succssfully!"

# Test video
echo "Testing YOLOv4 on video..."
echo ""
cd $DARKNET_REPO_PATH
python darknet_video.py --input $INPUT --out_filename $OUT_FILENAME --weights $WEIGHTS --dont_show --ext_output --config_file $CONFIG_FILE --data_file $DATA_FILE --thresh $THRESH

# Deactivate Conda Environment
echo "Deactivating Conda Environment..."
echo ""
conda deactivate

# Exit script
echo "Exiting script..."
echo ""
exit 0
