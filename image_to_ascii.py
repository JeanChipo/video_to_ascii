import os
from PIL import Image, ImageFilter

# ASCII_CHARS = "@%#*+=-:. "
ASCII_CHARS = ".,#/+-^~°`><;:_!\"$%&'()*"
# ASCII_CHARS = "!\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
# ASCII_CHARS = "Æ"


def resize_image(image, new_width=100):
    width, height = image.size
    aspect_ratio = height / width
    new_height = int(aspect_ratio * new_width * 0.55)
    return image.resize((new_width, new_height))

def grayify(image):
    """
    Convert image to grayscale.
    """
    return image.convert("L")

def edge_detection(image):
    return image.filter(ImageFilter.FIND_EDGES)

def thresdhold(image):
        return image.convert('L')

def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        return 128 + factor * (c - 128)

    return img.point(contrast)
def pixels_to_ascii(image):
    """
    Convert image pixels to ASCII characters.
    """
    pixels = image.getdata()
    grayscale_pixels = [sum(pixel) // 3 for pixel in pixels]
    ascii_str = "".join(ASCII_CHARS[pixel * len(ASCII_CHARS) // 256] for pixel in grayscale_pixels)
    return ascii_str


def apply_filters(image_path, width, filter_list:list):
    try:
        image = Image.open(image_path)
    except Exception as e:
        print(f"Unable to open image {image_path}. Error: {e}")
        return None
    
    image = resize_image(image, new_width=width)
    while filter_list != []:
        match filter_list[0]:
            case 1: 
                image = grayify(image)
                filter_list.pop(0)
            case 2: 
                image = edge_detection(image)
                filter_list.pop(0)
            case 3: 
                image = change_contrast(image, 100)
                filter_list.pop(0)
            case 4: 
                image = thresdhold(image)
                filter_list.pop(0)
            case 5: 
                image = image.convert('1') # To mono
                filter_list.pop(0)

            
    return image

def image_to_ascii(image_path, width=100, filter_list=[3]):
    """
    Convert an image file to ASCII art.
    """
    image = apply_filters(image_path, width, filter_list)
    ascii_str = pixels_to_ascii(image)
    ascii_art = "\n".join(ascii_str[i:i+width] for i in range(0, len(ascii_str), width))
    return ascii_art

def process_images_to_ascii(total_frames, images_dir, output_file, filter_list, width=100):
    """
    Convert all images in a directory to ASCII art and save them to a text file.
    """
    images = sorted([os.path.join(images_dir, img) for img in os.listdir(images_dir) if img.endswith(('.png', '.jpg', '.jpeg'))])
    if not images:
        print(f"No images found in directory: {images_dir}")
        return

    with open(output_file, "w") as file:
        for index, image_path in enumerate(images):
            print(f"Processing {image_path}, {int(1+(index/total_frames)*100)}%     ", end="\r")
            ascii_art = image_to_ascii(image_path, width)
            if ascii_art:
                file.write(ascii_art)
                file.write("\n" + ("=" * width) + "\n")
            else:
                print(f"Skipping {image_path}")

    print(f"\nASCII art saved to {output_file}")
