import csv
import random
import os

################################################################################
# This code is not necessary but we it help us to have balanced
# dataset 50%/50% action no action. This is useful in the track_1
################################################################################

# Location of csv file where we have saved out data from simulator
data_file = "driving_log_1_straight_relative"

# Keep track of amount of zero steering angle and non zero angle images
zero_steering = 0
non_zero_steering = 0

# We want to pick randomly so we will shuffle the data
to_shuffle = []
# Read CSV File and save the data
with open(f'{data_file}.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Keep track of amount of images with steering "action" and no steering "no action"
        if float(row[3]) == 0.0:
            zero_steering += 1
        else:
            non_zero_steering += 1
        to_shuffle.append(row)

    # Shuffling the data
    random.shuffle(to_shuffle)

    # Out new dataset will be the biggest possible 50%/50% dataset
    minimum_of_two = min(zero_steering,non_zero_steering)

    # So now we will count down zero angles and non zero angles, after
    # their count is bigger than minimum we will be deleting images
    countdown_angle = minimum_of_two
    countdown_noangle = minimum_of_two

    new_dataset = []
    deleted_images = 0

    for row in to_shuffle:
        # Shuffle the data and create a new dataset which will have the same number of "steering" instances and "no steering" instances
        if float(row[3]) == 0.0:
            if countdown_noangle > 0:
                new_dataset.append(row)
                countdown_noangle -= 1
        else:
            if countdown_angle > 0:
                new_dataset.append(row)
                countdown_angle -= 1

    with open(f'{data_file}_cleaned.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in new_dataset:
            filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])

    print(f"Done. New directory has length {minimum_of_two*2} and is saved in {data_file}.csv")
