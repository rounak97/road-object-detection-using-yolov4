# Road Object Detection Using YoloV4

[![Project Status: Active – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

The goal of this project is to detect Road Objects using [Yolov4](https://github.com/AlexeyAB/darknet). The network is trained on [Berkley DeepDrive Dataset](https://bdd-data.berkeley.edu/).

## Datasets
### Berkley DeepDrive Dataset [[Link](https://bdd-data.berkeley.edu/index.html)]
The Berkely DeepDrive Dataset is a dataset for evaluating image recognition algorithms' exciting progress on autonomous driving. The dataset possesses geographic, environmental, and weather diversity, which is useful for training models that are less likely to be surprised by new conditions. The dataset is the largest driving video dataset with 100K videos and 10 tasks. The video sequences also include GPS locations, IMU data, and timestamps. The 2D Bounding Boxes are annotated on the images for bus, traffic light, traffic sign, person, bike, truck, motor, car, train, and rider.

## Requirements
The code is based on Python3 (>=3.7). There are a few dependencies to run the code. The major libraries are listed as follows:
* Tensorflow (>=2.3.0)

## Installation Guide
To install the anaconda environment, navigate to the repository folder, and run the following command in the command prompt:

`conda env create -f environment.yml`

## Execution Guide
1. To activate the Conda environment, please run the following command in the command prompt:

`conda activate yolo`

2. *To be added*

3. To deactivate the Conda environment, please run the following command in the command prompt:

`conda deactivate`

## Clean-up Guide
To remove the anaconda environment, navigate to the repository folder, and run the following command in the command prompt:

`conda remove --name yolo --all`

## Authors
* Sourab Bapu Sridhar

## Acknowledgements
*To be added*

## License
This project is released under the terms of [MIT License](LICENSE).

