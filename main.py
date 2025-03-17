from vid_to_image import extract_frames
from image_to_ascii import process_images_to_ascii
from printing_image import printvid
from os.path import join, dirname, abspath

def get_user_input():
    while True:
        user_input = input("Here is the list of every filter available:\n"
                           "    1) grayify         - Convert image to grayscale.\n"
                           "    2) edge_detection  - Uses edge detection on the image.\n"
                           "    3) change_contrast - Makes it much easier for the program to detect color. RECOMMENDED.\n"
                           "    4) threshold       - Segments the image based on intensity values.\n"
                           "    5) mono            - Image is either white or black, no in-between.\n"
                           "Enter the filters you want to apply (separated by spaces, e.g., 1 2 3): \n>")
        input_list = user_input.split()
        try:
            filter_list = list(map(int, input_list))
            if all(1 <= f <= 5 for f in filter_list):
                return filter_list
            else:
                print("Error: All filter numbers must be between 0 and 5.")
        except ValueError:
            print("Error: Please enter valid integers separated by spaces.")


if __name__ == '__main__':
    video_file = input("Enter the path to the video file: \n>")
    total_frames = extract_frames(video_file)

    images_folder = join(dirname(abspath(__file__)), "images")
    output_txt_file = join(dirname(abspath(__file__)), "ascii_art.txt")
    width = int(input("Enter the width of the ASCII art: \n>"))
    filter_list = list(map(int, get_user_input()))
    process_images_to_ascii(total_frames, images_folder, output_txt_file, filter_list, width)
    
    if input("Do you want to print the resulting video now ? (y/n) \n>").lower() == 'y': 
        printvid()
        print("You can see the ascii video again by running show_results.py")
    else: print("You can execute show_results.py to visualize the results."
                " Tip: if your ascii art is to wide for your IDE terminal, use a separate one like windows' cmd and use ctrl+scroll back.")
