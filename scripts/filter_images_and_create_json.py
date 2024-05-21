import os
import sys
import json
import cv2
from helper.match_with_border import compare_borders
from helper.get_center_region import get_center_region
from helper.check_for_name_line import is_no_yellow_line
from helper.convert_image_to_array import image_to_2d_array

def extract_sort_key(filename):
    try:
        return int(filename.split('.')[0].split('_')[0])
    except ValueError:
        return float('inf')
    
def load_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def save_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file)
    
# take image of board and turn it into a 2d array
# make one json for these 2d arrays
def write_boards_to_master_json(board_files, image_dir_name):
    boards = []
    for filename in board_files:
        img_path = os.path.join(image_dir_name, filename)
        
        board = image_to_2d_array(img_path.strip())
        if any(sum(row) == 10 for row in board):
            continue
        
        boards.append(board)

    master_json='all_boards.json'
    if os.path.exists(master_json):
        master_data = load_json(master_json)
        boards.extend(master_data)

    save_json(boards, master_json)

def is_piece_spawn(img_path, reference_border, known_dark_image):
    return compare_borders(img_path, reference_border) and get_center_region(img_path, known_dark_image) and is_no_yellow_line(img_path)

# create a txt that holds all valid (mainly) boards
def get_board_files(image_dir_name, reference_border, known_dark_image):
    if not os.path.isdir(image_dir_name):
        return
    
    # Get the list of files in the directory
    files = sorted(os.listdir(image_dir_name), key=extract_sort_key)

    board_files = []
    prev_filename = files[0]
    wait = False
    cnt = 0
    for filename in files[1:]:
        img_path = os.path.join(image_dir_name, filename)
        if wait:
            cnt += 1
            if cnt > 8:
                wait = False
                cnt = 0
        # if board border is present, and a piece just spawned, save the previous image
        # also check for ctwc stats screen, do not save the stats screen
        elif is_piece_spawn(img_path, reference_border, known_dark_image):
            board_files.append(prev_filename)
            wait = True

        prev_filename = filename
    
    return board_files

def filter_main(image_dir_name, reference_border, known_dark_image):
    board_files = get_board_files(image_dir_name, reference_border, known_dark_image)
    write_boards_to_master_json(board_files, image_dir_name)

if __name__ == '__main__':
    image_dir_name = sys.argv[1]
    script_dir = os.path.dirname(os.path.abspath(__file__))

    reference_border_path = os.path.join(script_dir, 'helper', 'gray_border.png')
    reference_border = cv2.cvtColor(cv2.imread(reference_border_path), cv2.COLOR_BGR2GRAY)

    known_dark_image_path = os.path.join(script_dir, 'helper', 'black_center_region.jpg')
    known_dark_image = cv2.cvtColor(cv2.imread(known_dark_image_path), cv2.COLOR_BGR2GRAY)

    filter_main(image_dir_name, reference_border, known_dark_image)
