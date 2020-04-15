# Improting Image class from PIL module 
from PIL import Image
import cv2
import os


# Opens a image in RGB mode
#GRIZLI postage stamps are 340 pixels tall and 1 extraction is 300 pixels wide
directory = "/Users/jennifercooper/Projects/thesis/23.3_mag/all/Extractions/images/test"
#im = Image.open(r"/Users/jennifercooper/Projects/thesis/23.3_mag/all/Extractions/images/test/j105836m1254_00260.line.png") 
#width, height = im.size
#im.show()
#print(im.size)
count = 0
# Setting the points for cropped image
# First emission line box parameters
left = 325
top = 1
right = 607
bottom = 310
output_dir = "/Users/jennifercooper/Projects/thesis/23.3_mag/all/Extractions/images/single/"

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith("line.png"):
        # Cropped image of above dimension 
        # (It will not change orginal image)
        filepath = os.path.join(directory,filename)
        im = Image.open(filepath)
        im1 = im.crop((left, top, right, bottom)).save(output_dir+"crop1_"+file)
# Shows the image in image viewer 
#im1.show() 
