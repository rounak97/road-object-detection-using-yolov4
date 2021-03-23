# Road Object Detection Using YOLOv4

[![Project Status: Active – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

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
1. To activate the Conda environment, please run the following command in the terminal:

```
$conda activate yolo
```

2. Train the YOLOv4 network in the Conda environment using by the following the instructions [here](https://github.com/sourabbapusridhar/road-object-detection-using-yolov4#training-the-yolov4-network).

3. Test the YOLOv4 network in the Conda environment using by the following the instructions [here](https://github.com/sourabbapusridhar/road-object-detection-using-yolov4#testing-the-yolov4-network).

4. To deactivate the Conda environment, please run the following command in the terminal:

```
$conda deactivate
```

## Training the YOLOv4 network
1. To clone the official implementation of YOLOv4 Neural Network from AlexeyAB's darknet repository and the Road Object Detection Using YoloV4 repository, run the following command in the terminal:

```
$git clone https://github.com/AlexeyAB/darknet.git    # Official YOLOv4 Implementation
$git clone https://github.com/sourabbapusridhar/road-object-detection-using-yolov4.git      # Road Object Detection Using YoloV4 repository
```

2. For training on a GPU, the parameters `OPENCV`, `GPU`, `CUDNN` need to be set in the Makefile. The parameter `CUDNN_HALF` can also be set in the Makefile to use the Tensor Cores. To set the paramters mentioned above, run the following commands in the terminal:

```
$cd darknet
$sed -i 's/OPENCV=0/OPENCV=1/' Makefile
$sed -i 's/GPU=0/GPU=1/' Makefile
$sed -i 's/CUDNN=0/CUDNN=1/' Makefile
$sed -i 's/CUDNN_HALF=0/CUDNN_HALF=1/' Makefile
```

3. To build Darknet, please run the following command in the terminal:

```
$cd darknet
$make
```

4. For training `cfg/yolov4-custom.cfg` or `yolov4-tiny-custom.cfg`, download the corresponding pretrained weights file using the following commands in the terminal:

```
$cd darknet
$wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v3_optimal/yolov4.conv.137     # For training cfg/yolov4-custom.cfg
$wget https://github.com/AlexeyAB/darknet/releases/download/darknet_yolo_v4_pre/yolov4-tiny.conv.29     # For training cfg/yolov4-tiny-custom.cfg
```


## Testing the YOLOv4 network
*To be added*

## Clean-up Guide
To remove the anaconda environment, navigate to the repository folder, and run the following command in the terminal:

```
$conda remove --name yolo --all
```

## Authors
* Sourab Bapu Sridhar

## Acknowledgements
*To be added*

## License
This project is released under the terms of [MIT License](LICENSE).

