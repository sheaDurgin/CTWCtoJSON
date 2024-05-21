import cv2
import numpy as np
from skimage.metrics import structural_similarity
import sys
import os
import random

def get_gray_border(image_filename):
    image = cv2.cvtColor(cv2.imread(image_filename), cv2.COLOR_BGR2GRAY)
    height, width = image.shape

    alpha_channel = np.zeros((height, width), dtype=image.dtype)

    alpha_channel[:2, :] = 255  # Top 2px rows
    alpha_channel[-2:, :] = 255  # Bottom 2px rows
    alpha_channel[:, :2] = 255  # Left 2px columns
    alpha_channel[:, -2:] = 255  # Right 2px columns

    gray_border = cv2.merge((image, image, image, alpha_channel))
    return gray_border[:,:,0]

def compare_borders(target_image_path, reference_border, threshold=0.60):
    target_border = get_gray_border(target_image_path)

    if target_border is None:
        return False

    score = structural_similarity(reference_border, target_border)
    return True if score > threshold else False

if __name__ == '__main__':
    target_image_path = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))
    reference_border_path = os.path.join(script_dir, 'gray_border.png')
    reference_border = cv2.cvtColor(cv2.imread(reference_border_path), cv2.COLOR_BGR2GRAY)

    if compare_borders(target_image_path, reference_border):
        print(f"Border of target_image matches the reference border")