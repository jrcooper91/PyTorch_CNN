# Function to extract frames from input video file and save them as separate frames in an output directory.
import cv2
import time
import os

def video_to_frames(input_loc, output_loc):
    try:
        os.mkdir(output_loc)
    except OSError:
        pass
    # Log the start time
    time_start = time.time()
    # Start capturing the feed
    cap = cv2.VideoCapture(input_loc)
    # Find the number of frames
    video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1 #this is required or else it will find an empty frame
    print ("Number of frames: ", video_length) #divide this by the fps to get video length. Model 3 sentry mode with HW 3.0 hardware records at 36 fps = 1 minute clip.
    count = 0
    print ("Converting video..\n")
    # Start converting the video
    while cap.isOpened():
        # Extract the frame
        ret, frame = cap.read()
        # Write the results back to output location.
        cv2.imwrite(output_loc + "/%#05d.jpg" % (count+1), frame)
        count = count + 1
        # If there are no more frames left
        if (count > (video_length-1)):
            # Log the time again
            time_end = time.time()
            # Release the feed
            cap.release()
            # Print stats
            print ("Done extracting frames.\n%d frames extracted" % count)
            print ("It took %d seconds forconversion." % (time_end-time_start))
            break

if __name__=="__main__":
    input_loc = '/Users/jennifercooper/Projects/Tesla/Driving/2020-04-01_12-59-14-front.mp4'
    output_loc = '/Users/jennifercooper/Projects/Tesla/PyTorchTraining/Potholes/data'
    video_to_frames(input_loc, output_loc)
