import cv2
import numpy as np
from skimage.metrics import structural_similarity
import sys
import os
import random

def get_gray_border(image_filename):
    image = cv2.imread(image_filename)

    height, width, _ = image.shape

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    alpha_channel = np.zeros((height, width), dtype=image.dtype)

    alpha_channel[:2, :] = 255  # Top 2px rows
    alpha_channel[-2:, :] = 255  # Bottom 2px rows
    alpha_channel[:, :2] = 255  # Left 2px columns
    alpha_channel[:, -2:] = 255  # Right 2px columns

    n1 = str(random.randint(1, 99999))
    n2 = str(random.randint(1, 99999))

    new_filename = n1 + 'temp_border' + n2 + '.png' 

    gray_border = cv2.merge((gray_image, gray_image, gray_image, alpha_channel))
    cv2.imwrite(new_filename, gray_border)
    return cv2.cvtColor(cv2.imread(new_filename), cv2.COLOR_BGR2GRAY), new_filename

def compare_borders(target_image_path, threshold=0.60):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    reference_border_path = os.path.join(script_dir, 'gray_border.png')
    
    reference_border = cv2.cvtColor(cv2.imread(reference_border_path), cv2.COLOR_BGR2GRAY)
    target_border, delete_filename = get_gray_border(target_image_path)

    if target_border is None or delete_filename is None:
        return False

    score = structural_similarity(reference_border, target_border)
    os.remove(delete_filename)
    return True if score > threshold else False

if __name__ == '__main__':
    target_image_path = sys.argv[1]

    if compare_borders(target_image_path):
        print(f"Border of target_image matches the reference border")