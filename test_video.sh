#!/bin/bash

#####################################################################################################################
######################################## UPDATE BELOW PATHS BEFORE RUNNING ##########################################
#####################################################################################################################

# Provide full paths to the road-object-detection-using-yolov4 repository
ROAD_REPO_PATH=/home/sourab/Data/repos/road-object-detection-using-yolov4      #e.g. /home/user/repo-name

# Provide full path to the input video (Set to 0 for using WEBCAM)
INPUT_VIDEO=/home/sourab/Data/temp/test/test-video.avi                         #e.g. /home/user/video.avi

# Provide full path to the weights file
WEIGHTS_PATH=$ROAD_REPO_PATH/weights/yolov4-tiny-bdd100k_best.weights          #e.g. /home/user/darknet/backup/

# Provide full path to the config file
CONFIG_PATH=$ROAD_REPO_PATH/config/yolov4-tiny-bdd100k.cfg                     #e.g. /home/user/darknet/cfg/

# Provide full path to the labels file
LABELS_PATH=$ROAD_REPO_PATH/data/bdd100k.names                                 #e.g. /home/user/darknet/config/

#####################################################################################################################
######################################## UPDATE BELOW FLAGS BEFORE RUNNING ##########################################
#####################################################################################################################

# Set a value of confidence threshold to remove detections with lower confidence
CONFIDENCE_THRESH=0.5                                                          #e.g. 0.1, 0.2, 0.3...

# Set a value of non-maximum suppression threshold to reduce false positives 
NMS_THRESHOLD=0.3                                                              #e.g. 0.1, 0.2, 0.3...

#####################################################################################################################
######################################## DO NOT MODIFY THE SETTINGS BELOW ###########################################
#####################################################################################################################

# Print current path and provided path
echo "Printing paths and flags set..."
echo "Path to the road-object-detection-using-yolov4 repository: $ROAD_REPO_PATH"
echo "Path to the input video: $INPUT_VIDEO"
echo "Path to the weights file: $WEIGHTS_PATH"
echo "Path to the config file: $CONFIG_PATH"
echo "Path to the labels file: $LABELS_PATH"
echo "Value of confidence threshold: $CONFIDENCE_THRESH"
echo "Value of non-maximum suppression threshold: $NMS_THRESHOLD"
echo ""

# Activate conda virtual environment to run from bash
echo "Initializing conda virtual environment to run from bash..."
echo ""
conda init bash && echo "Conda virtual environment initialized successfully!"

# Activating the conda virtual environment
echo "Activating the conda virtual environment..."
echo ""
source ~/Data/miniconda3/etc/profile.d/conda.sh                # Workaround (conda activate does not work from bash)
conda activate yolo && echo "Conda virtual environment activated successfully!"

# Test YOLOv4 on an image
echo "Testing YOLOv4 on an image..."
echo ""
cd $ROAD_REPO_PATH
python detection.py --nnWeights $WEIGHTS_PATH --nnConfiguration $CONFIG_PATH --labelsPath $LABELS_PATH --confidenceThreshold $CONFIDENCE_THRESH --nmsThreshold $NMS_THRESHOLD --videoPath $INPUT_IMAGE

# Deactivate conda virtual environment
echo "Deactivating Conda virtual environment..."
echo ""
conda deactivate

# Exit script
echo "Exiting script..."
echo ""
exit 0
