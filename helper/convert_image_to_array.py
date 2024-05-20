import cv2
import sys

def image_to_2d_array(image_path, threshold=10):
    image = cv2.imread(image_path)

    cropped_resized_image = image[2:image.shape[0]-2, 2:image.shape[1]-2]
    resized_image = cv2.resize(cropped_resized_image, (10, 20))

    grayscale_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

    _, binary_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)

    array_2d = (binary_image / 255).astype(int)

    return array_2d.tolist()

if __name__ == '__main__':
    image_path = sys.argv[1]
    tetris_board_array = image_to_2d_array(image_path)
    for row in tetris_board_array:
        print(row)
