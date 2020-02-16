# Resize all images in a directory
# pass directory of the images you want to resize as argv
import os
import sys
import cv2

directory = sys.argv[1]

# SPECIFY THE NEW IMG DIMENSIONS (Width, Height)
new_dim = [80, 40]

processed = 0
for file_name in os.listdir(directory):
  print("Processing", file_name)
  # Read image
  image = cv2.imread(os.path.join(directory, file_name))
  # Resize image
  resized_image = cv2.resize(image, (new_dim[0], new_dim[1]))
  # Save image
  output_file_name = os.path.join(directory, file_name)
  cv2.imwrite(output_file_name, resized_image)
  processed += 1

print(f"Done. Resized {processed} images in dir {directory}.")
