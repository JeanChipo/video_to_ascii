The goal of the repo is to input a video and output the same video in a ASCII art version.
This is done by :
1) extracting every frame of the video, as well as the fps for accurate output.
2) converting every frame extracted in a ASCII art form using filters from the PIL library 
3) printing each frame while clearing the screen based on the number of fps from the original video

### You will need the following python libraries for this program to work : **Time, os, PIL, cv2, glob**

## To run it:
Download the repo and execute `main.py`, all instructions will be given during the execution.
When asked the path to the video file, you are able to give it in quotes ("").

Also, if you need the output of any of the steps, they will be put in the folder where `main.py` is located :
If you need the frames, they will be in the `images` folder.
If you need the ascii art of each frames, it will be in the `ascii_art.txt` file.
