# Script to detect objects using YOLOv4

import os
import cv2
import argparse
import numpy as np

def extract_boxes_confidences_classids(outputs, confidenceThreshold, height, width):
    """
    Function to extract boxes, confidences and class Ids for all the detections.

    The function only extracts information for detections whose confidence is higher than 
    the thresholds defined as the argument.

    Parameters
    ----------
    outputs             : list
                          List of all the detections
    confidenceThreshold : float
                          Confidence threshold for discarding low confidence detections
    height              : int
                          Height of the input image
    width               : int
                          Width of the input image

    Returns
    -------
    boxes       : list
                  List of all the boxes for all the detections
    confidences : list
                  List of all the confidences for all the detections
    classIds    : list
                  List of all the classIds for all the detections
    """
    boxes = []
    confidences = []
    classIds = []

    for output in outputs:
        for detection in output:
            # Extract the scores, classId and individualConfidence of each detection
            scores = detection[5:]
            classId = np.argmax(scores)
            individualConfidence = scores[classId]

            # Consider detections with confidences higher than confidenceThreshold
            if individualConfidence > confidenceThreshold:
                # Scale the bounding box back to the size of the image
                box = detection[0:4] * np.array([width, height, width, height])
                centerX, centerY, w, h = box.astype("int")

                # Use the center coordinates and the height and width of the image to calculate the top left corner
                x = int(centerX - (w/2))
                y = int(centerY - (h/2))

                boxes.append([x, y, int(w), int(h)])
                confidences.append(float(individualConfidence))
                classIds.append(classId)

    return boxes, confidences, classIds


def make_prediction(net, layerNames, image, confidenceThreshold, nmsThreshold):
    """
    Function to make prediction about the objects in the image.

    The function only extracts information for detections whose confidence is higher than 
    the thresholds defined as the argument. Later, the function passes the detections through
    Non-Maximum Suppression algorithm to reduce the number of false positives.

    Parameters
    ----------
    net                 : cv2.dnn_net
                          Neural network to predict about the objects in the image
    layerNames          : list
                          Neural network output layers through which the input image needs to be passed
    image               :
                          Input image
    confidenceThreshold : float
                          Confidence threshold for discarding low confidence detections
    nmsThreshold        : float
                          Non-maximum Suppression threshold for reducing the number of false positives

    Returns
    -------
    boxes       : list
                  List of all the boxes for all the detections
    confidences : list
                  List of all the confidences for all the detections
    classIds    : list
                  List of all the classIds for all the detections
    ids         : list
                  List of all the ids for all the detections that make through the Non-Maximum Suppression algorithm
    """
    height, width = image.shape[:2]

    # Create a blob and pass it through the model
    blob = cv2.dnn.blobFromImage(image, 1/255.0, (416,416), swapRB=True, crop=False)
    net.setInput(blob)
    outputs = net.forward(layerNames)

    # Extract bounding boxes, confidences, classIds and pass it through a Non-Maximum Suppression algorithm
    boxes, confidences, classIds = extract_boxes_confidences_classids(outputs, confidenceThreshold, height, width)
    ids = cv2.dnn.NMSBoxes(boxes, confidences, confidenceThreshold, nmsThreshold)

    return boxes, confidences, classIds, ids

def draw_bounding_boxes(image, boxes, confidences, classIds, ids, labels, colors):
    """
    Function to draw bounding boxes.

    Parameters
    ----------
    image       :
                  Input image
    boxes       : list
                  List of all the boxes for all the detections
    confidences : list
                  List of all the confidences for all the detections
    classIds    : list
                  List of all the classIds for all the detections
    ids         : list
                  List of all the ids for all the detections that make through the Non-Maximum Suppression algorithm
    labels      : list
                  List of all the labels
    colors      : list
                  List of all the colors

    Returns
    -------
    image   :
              Image with the bounding boxes
    """
    if len(ids) > 0:
        for i in ids.flatten():
            x, y = boxes[i][0], boxes[i][1]
            w, h = boxes[i][2], boxes[i][3]

            color = [int(c) for c in colors[classIds[i]]]
            cv2.rectangle(image, (x,y), ((x+w), (y+h)), color, 2)
            text = "{}: {:.4f}".format(labels[classIds[i]], confidences[i])
            cv2.putText(image, text, (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    return image

def detect_objects(nnWeights, nnConfiguration, labelsPath, confidenceThreshold, nmsThreshold, imagePath, videoPath):
    """
    Function to detect objects from the image.

    Parameters
    ----------
    nnWeights           : str
                          Neural network weights
    nnConfiguration     : str
                          Neural network configuration
    labelsPath          : str
                          Paths to the labels file
    confidenceThreshold : float
                          Confidence threshold for discarding low confidence detections
    nmsThreshold        : float
                          Non-maximum Suppression threshold for reducing the number of false positives
    imagePath           : str
                          Path to the input image file
    videoPath           : str
                          Path to the input video file

    Returns
    -------
    None
    """
    with open(labelsPath, "r") as labelsFile:
        labels = labelsFile.read().strip().split("\n")
    
    colors = np.random.randint(0, 255, size=(len(labels),3), dtype="uint8")

    net = cv2.dnn.readNetFromDarknet(nnConfiguration, nnWeights)
    net.setPreferableBackend(cv2.dnn.DNN_BACKEND_CUDA)
    net.setPreferableTarget(cv2.dnn.DNN_TARGET_CUDA)

    layerNames = net.getLayerNames()
    layerNames = [layerNames[i[0] - 1] for i in net.getUnconnectedOutLayers()]

    os.makedirs("output", exist_ok=True)

    if imagePath is not None:
        image = cv2.imread(imagePath)

        boxes, confidences, classIds, ids = make_prediction(net, layerNames, image, confidenceThreshold, nmsThreshold)
        image = draw_bounding_boxes(image, boxes, confidences, classIds, ids, labels, colors)
        fileName = str(os.path.normpath(imagePath)).split("\\")[-1]

        cv2.imwrite("output/{}".format(fileName), image)
    else:
        if videoPath == "0":
            video =  cv2.VideoCapture(0)
        else:
            video = cv2.VideoCapture(videoPath)

        width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = video.get(cv2.CAP_PROP_FPS)
        fileName = str(os.path.normpath(videoPath)).split("\\")[-1].split(".")[0] + ".mp4" #if videoPath else "camera.avi"
        output = cv2.VideoWriter("output/{}".format(fileName), cv2.VideoWriter_fourcc("M", "P", "4", "V"), fps, (width, height))

        while video.isOpened():
            returnValue, image = video.read()

            if not returnValue:
                print("Video file finished...")
                break

            boxes, confidences, classIds, ids = make_prediction(net, layerNames, image, confidenceThreshold, nmsThreshold)
            image = draw_bounding_boxes(image, boxes, confidences, classIds, ids, labels, colors)

            output.write(image)

        video.release()
        output.release()

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
    parser = argparse.ArgumentParser(description="Script to detect objects using YOLOv4")
    parser.add_argument("-w", "--nnWeights", type=str, default="weights/yolov4-tiny-bdd100k_best.weights", help="Path to neural network weights")
    parser.add_argument("-cfg", "--nnConfiguration", type=str, default="config/yolov4-tiny-bdd100k.cfg", help="Path to neural network configuration")
    parser.add_argument("-l", "--labelsPath", type=str, default="data/bdd100k.names", help="Path to labels file")
    parser.add_argument("-c", "--confidenceThreshold", type=float, default=0.5, help="Minimum confidence required to detect objects")
    parser.add_argument("-n", "--nmsThreshold", type=float, default=0.3, help="Minimum threshold required for Non-Maximum Suppression")

    inputPath = parser.add_mutually_exclusive_group()
    inputPath.add_argument("-i", "--imagePath", type=str, default=None, help="Path to the input image file")
    inputPath.add_argument("-v", "--videoPath", type=str, default=None, help="Path to the input video file")

    args = parser.parse_args()

    detect_objects(args.nnWeights, args.nnConfiguration, args.labelsPath, args.confidenceThreshold, args.nmsThreshold, args.imagePath, args.videoPath)

if __name__ == "__main__":
    main()