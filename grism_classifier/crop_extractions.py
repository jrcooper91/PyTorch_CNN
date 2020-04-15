# Improting Image class from PIL module 
from PIL import Image
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
#stellar map line box paramters
left0 = 1
top0 = 1
right0 = 301
bottom0 = 310
# First emission line box parameters
left1 = 325
top1 = 1
right1 = 607
bottom1 = 310
# Second emission line
left2 = 607
top2 = 1
right2 = 907
bottom2 = 310
# Third emission line
left3 = 907
top3 = 1
right3 = 1207
bottom3 = 310

#where to save the files
output_dir_em = "/Users/jennifercooper/Projects/thesis/23.3_mag/all/Extractions/images/single/" #emission line map extractions
output_dir_st = "/Users/jennifercooper/Projects/thesis/23.3_mag/all/Extractions/images/stellar/" #emission line map stellar

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith("line.png"):
        # Cropped image of above dimension 
        # (It will not change orginal image)
        filepath = os.path.join(directory,filename)
        im = Image.open(filepath)
        width, height = im.size
        if width in range(301,1600):
            im1 = im.crop((left1, top1, right1, bottom1)).save(output_dir_em+"crop1em_"+file)
        if width in range(601,1600):
            im2 = im.crop((left2, top2, right2, bottom2)).save(output_dir_em+"crop2em_"+file)
        if width in range(901,1600):
            im3 = im.crop((left3, top3, right3, bottom3)).save(output_dir_em+"crop3em_"+file)
# Shows the image in image viewer 
#im1.show() 
