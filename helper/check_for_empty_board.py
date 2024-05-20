import cv2
import numpy as np
import sys

def is_almost_black(filename, threshold=0.8):
    image = cv2.imread(filename)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    height, _ = gray_image.shape

    num_black_pixels = np.sum(gray_image[height // 2:, :] == 0)

    proportion_black = num_black_pixels / gray_image.size
    print(proportion_black)
    return proportion_black >= threshold

if __name__ == "__main__":
    result = is_almost_black(sys.argv[1])
    print(result)