import cv2
import os
from glob import glob

def reformat(video_path:str)->str:
    """
    Remove quotes from the input string if they exist.
    """
    if video_path[0]=='"' or video_path[len(video_path)-1]=='"':
        return video_path[1:-1]

def extract_frames(video_path: str) -> int:
    """
    Create the images directory, clear existing frames, and extract new frames.
    """
    video_path = reformat(video_path)
    script_dir = os.path.dirname(os.path.abspath(__file__))
    images_dir = os.path.join(script_dir, 'images')

    if not os.path.exists(images_dir):
        os.makedirs(images_dir)
    else:
        # Clear existing frames in the images directory
        files = glob(os.path.join(images_dir, '*.jpg'))
        for file in files:
            os.remove(file)

    video_capture = cv2.VideoCapture(video_path)
    if not video_capture.isOpened():
        print(f"Error: Could not open video \"{video_path}\", make sure that the path is valid.")
        return

    frame_count = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = video_capture.get(cv2.CAP_PROP_FPS)
    print(f"Total frames: {frame_count}, FPS: {fps}")

    frame_index = 0

    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        frame_filename = os.path.join(images_dir, f'frame_{frame_index:04d}.jpg')
        cv2.imwrite(frame_filename, frame)

        print(f"Extracted: {frame_filename}, {int(1+(frame_index/frame_count)*100)}%    ", end='\r')
        frame_index += 1

    video_capture.release()
    print(f"\nFrames saved in {images_dir}")

    return frame_count


# if __name__ == "__main__":
#     video_file = input("Enter the path to the video file: ")
#     extract_frames(video_file)
