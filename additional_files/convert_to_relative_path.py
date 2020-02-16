import csv
import os

################################################################################
# This code reads all the images in a given dataset
# and converts the path from the original images to the new specified path
################################################################################
# Location of csv file where we have saved out data log from simulator *path prefix*
# use_path is the path we want to attach to our image location *path sufix*

data_file = "driving_log_track_2_full_relative.csv"
use_path = r"dataset\track_2\images"

################################################################################

# Read CSV File and save the data
with open(f'{data_file}', 'r') as file:
    new_dataset = []
    reader = csv.reader(file)

    # Iterate csv file
    for row in reader:
        center_img_name = row[0].split("\\")[-1]
        left_img_name = row[1].split("\\")[-1]
        right_img_name = row[2].split("\\")[-1]

        new_center_img_path = os.path.join(use_path, center_img_name)
        new_left_img_path = os.path.join(use_path, left_img_name)
        new_right_img_path = os.path.join(use_path, right_img_name)

        row[0] = new_center_img_path
        row[1] = new_left_img_path
        row[2] = new_right_img_path

        new_dataset.append(row)
    # Write new csv file with relative paths
    with open(f'driving_log_track_2_full_relative_rep.csv', 'w', newline='') as csvfile:
        filewriter = csv.writer(csvfile, delimiter=',',
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for row in new_dataset:
            filewriter.writerow([row[0], row[1], row[2], row[3], row[4], row[5], row[6]])
