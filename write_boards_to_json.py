import os
import sys
import json
from helper.convert_image_to_array import image_to_2d_array
    
# take image of board and turn it into a 2d array
# make one json for these 2d arrays
def write_boards_to_json(txt_file):
    if not os.path.exists('jsons/'):
        os.makedirs('jsons/')
    if not os.path.exists(txt_file):
        return
    
    dir_name = os.path.dirname(txt_file) + '/'

    with open(txt_file, 'r') as f:
        files = f.readlines()

    boards = []
    for filename in files:
        img_path = dir_name + filename
        
        board = image_to_2d_array(img_path.strip())
        if any(sum(row) == 10 for row in board):
            continue
        
        boards.append(board)
    
    output_file = os.path.dirname(dir_name)
    if not output_file:
        output_file = txt_file.split('.')[0]
    with open('jsons/' + output_file + '.json', 'w') as f:
        json.dump(boards, f)

if __name__ == '__main__':
    write_boards_to_json(sys.argv[1])