import sys
import cv2
import os
from convert_video_to_images import convert_video_to_images
from filter_images_and_create_json import filter_main

if __name__ == '__main__':
    video_path = sys.argv[1]
    year = sys.argv[2]
    boards_dir_name = sys.argv[3]

    print("Converting video to board images")
    board_dir_path1, board_dir_path2 = convert_video_to_images(video_path, year, boards_dir_name)

    script_dir = os.path.dirname(os.path.abspath(__file__))

    border_name = f"{year}_gray_border.png"
    reference_border_path = os.path.join(script_dir, 'helper', border_name)
    reference_border = cv2.cvtColor(cv2.imread(reference_border_path), cv2.COLOR_BGR2GRAY)

    known_dark_image_path = os.path.join(script_dir, 'helper', 'black_center_region.jpg')
    known_dark_image = cv2.cvtColor(cv2.imread(known_dark_image_path), cv2.COLOR_BGR2GRAY)

    print("Filtering images and writing to all_boards.json for board 1")
    filter_main(board_dir_path1, reference_border, known_dark_image)

    print("Filtering images and writing to all_boards.json for board 2")
    filter_main(board_dir_path2, reference_border, known_dark_image)

    print("Completed writing/appending to all_boards.json")