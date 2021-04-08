# Road Object Detection Using YOLOv4

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip) [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/sourabbapusridhar/road-object-detection-using-yolov4/blob/master/colab/yolov4_bdd100k.ipynb)

The goal of this project is to detect Road Objects using [YOLOv4](https://github.com/AlexeyAB/darknet). The network is trained on [Berkley DeepDrive Dataset](https://bdd-data.berkeley.edu/).

## Dataset
### Berkley DeepDrive Dataset [[Link](https://bdd-data.berkeley.edu/index.html)]:
The Berkely DeepDrive Dataset is a dataset for evaluating image recognition algorithms' exciting progress on autonomous driving. The dataset possesses geographic, environmental, and weather diversity, which is useful for training models that are less likely to be surprised by new conditions. The dataset is the largest driving video dataset with 100K videos and 10 tasks. The video sequences also include GPS locations, IMU data, and timestamps. The 2D Bounding Boxes are annotated on the images for bus, traffic light, traffic sign, person, bike, truck, motor, car, train, and rider.

- **Full Dataset and Annotations:** https://bdd-data.berkeley.edu/index.html#download-section

**Important:** The videos, images and the labels are only used for educational, research and not-for-profit purposes.

## Requirements
The code is based on Python3 (>=3.7). There are a few dependencies to run the code. The major libraries are listed as follows:
* Tensorflow (>=2.3.0)

## Installation Guide
To install the anaconda environment, navigate to the repository folder, and run the following command in the terminal:

```
$conda env create -f environment.yml
```

## Execution Guide
1. Train the YOLOv4 network in the Conda environment using by the following the instructions [here](https://github.com/sourabbapusridhar/road-object-detection-using-yolov4#training-the-yolov4-network).

2. Test the YOLOv4 network in the Conda environment using by the following the instructions [here](https://github.com/sourabbapusridhar/road-object-detection-using-yolov4#testing-the-yolov4-network).

## Training the YOLOv4 network
To train the YOLOv4 network on the Berkley DeepDrive dataset in the Conda environment, please update the paths and flags in the script `train.sh` and run the following command in the terminal:

```
$bash train.sh
```

## Testing the YOLOv4 network
### Test on an image
To test the YOLOv4 network on an image in the Conda environment, please update the paths and flags in the script `test_image.sh` and run the following command in the terminal:

```
$bash test_image.sh
```

### Test on a video
To test the YOLOv4 network on a video in the Conda environment, please update the paths and flags in the script `test_video.sh` and run the following command in the terminal:

```
$bash test_video.sh
```

## Clean-up Guide
To remove the anaconda environment, navigate to the repository folder, and run the following command in the terminal:

```
$conda remove --name yolo --all
```

## Authors
* Sourab Bapu Sridhar

## Acknowledgements
The code in this repository is based 

## License
This project is released under the terms of [MIT License](LICENSE).

