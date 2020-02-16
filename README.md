# Udacity Self Driving Simulator with PyTorch

![alt text](https://github.com/PeterKillerio/Udacity_Self-Dirivng_Car_Simulator_with_PyTorch/blob/master/github_images/track_1.png)

![alt text](https://github.com/PeterKillerio/Udacity_Self-Dirivng_Car_Simulator_with_PyTorch/blob/master/github_images/track_2.png)

libraries used:
cv2
tqdm
pytorch
matplotlib
numpy
socketio
PIL
flask

This is a PyTorch (CUDA READY - training/using model) implementation of a behavioral cloning with convolutional neural networks.
Repository includes all the necessary Python files as well as already trained models and datasets for training (track 1 and track 2).

Simulator can be downloaded here: https://github.com/udacity/self-driving-car-sim

Information about the datasets/datalogs can be found in "datalogs_info.txt" file in the main directory.
In those datalogs there is saved all the information needed for training: path to the center image, steering angle for that particular image, throttle value and speed.

Files in the main directory with suffix "_color" are files needed in order to train, change model architecture, load data and use colored images for driving.
Other files without the suffix are files needed in order to train, change model architecture, load data and use grayscale images for driving.

Drive.py / Drive_color.py - Are the files used to start the communication between the car simulator and the trained model. You have to specify the input resolution which your model uses. For the communication to initialize you have to have udacity-car-simulator opened up and running in autonomous mode. This code is copied from repository https://github.com/llSourcell/How_to_simulate_a_self_driving_car 

model_architecture.py / model_architecture_color.py - Are the files in which you can define you neural network architecture for your model.

prepare_data.py / prepare_data_color.py - Are the files necessary for you to load data (images, steering angle, throttle, speed) for training. In these files you have to specify which datalog will you use to load images, resolution etc.. as well as how many images/data rows you want to use and how you want to divide training/validation datasets.

Train_model.py / Train_model_color.py - Are the files used for training, these files import and use prepare_data.py / prepare_data_color.py files to load training data. In these files you can change the training function/ define hyperparameters etc... and the name for the saved model.

additional_files/clean_track_1_dataset.py - Is the file used to "clean" the dataset/datalog for the track 1. The way it cleans the dataset is that while driving on the track 1, the user (while using keyboard) mostly produces 0 steering angle. I wanted to have 50%/50% distributed in action/no action - 0 steering angle/ no 0 steering angle  and I think this improved my model a bit.
To use this file, you have to provide path to the csv file you want to clean and choose the name for the output csv file.

additional_files/convert_to_relative_path.py - Converts datalogs paths of the images to relative paths of the same images. This file is not necessary but needed for sharing purposes because if anybody wants to use your dataset they won't be able to because they don't have the same directory as you.

additional_files/resize_images.py - Is important file which resizes all the images in specified directory which you pass as an argument to the file. Resized images replace all the older files. You can specify the resolution you want to resize images to and it should be the resolution on which you want to train your model.

additional_files/utils.py - I didn't change anything in this file and is copied from repository https://github.com/llSourcell/How_to_simulate_a_self_driving_car  This file works with Drive.py / Drive_color.py to initialize communication between unity simulator and python.



