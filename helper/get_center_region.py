import cv2
import sys
import numpy as np
import os

def is_brighter_than_dark(image):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    known_dark_image_path = os.path.join(script_dir, 'black_center_region.jpg')
    
    known_dark_image = cv2.imread(known_dark_image_path)
    known_dark_image = cv2.cvtColor(known_dark_image, cv2.COLOR_BGR2GRAY)

    avg_intensity_test = np.mean(image)
    avg_intensity_known = np.mean(known_dark_image)

    threshold = 20

    return avg_intensity_test > (avg_intensity_known + threshold)

def get_center_region(filename):
    image = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2GRAY)

    _, width = image.shape

    start_x = (width - 90) // 2
    start_y = 4

    center_region = image[start_y:start_y+36, start_x+25:start_x+65]

    return is_brighter_than_dark(center_region)

if __name__ == '__main__':
    print(get_center_region(sys.argv[1]))
