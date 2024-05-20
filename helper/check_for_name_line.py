import cv2
import numpy as np
import sys

def is_transparent(image):
    if image is None or image.shape[2] != 4:
        return False

    if np.all(cv2.split(image)[3] == 0):
        return True
    
    return False

def is_no_yellow_line(image_filename):
    image = cv2.imread(image_filename)

    if image is None:
        print("Error: Unable to read image.")
        return False

    height, width, _ = image.shape

    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    mask = cv2.inRange(hsv_image, lower_yellow, upper_yellow)

    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    alpha_channel = np.zeros((height, width), dtype=image.dtype)

    for contour in contours:
        if cv2.boundingRect(contour)[1] < height // 4:
            cv2.drawContours(alpha_channel, [contour], -1, 255, thickness=cv2.FILLED)

    image_with_alpha = cv2.merge((image[:, :, 0], image[:, :, 1], image[:, :, 2], alpha_channel))

    return is_transparent(image_with_alpha)

if __name__ == '__main__':
    image_path = sys.argv[1]
    print(is_no_yellow_line(image_path))