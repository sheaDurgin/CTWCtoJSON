import os
import sys
from helper.match_with_border import compare_borders
from helper.get_center_region import get_center_region
from helper.check_for_name_line import is_no_yellow_line

def extract_sort_key(filename):
    try:
        return int(filename.split('.')[0].split('_')[0])
    except ValueError:
        return float('inf')

# create a txt that holds all valid (mainly) boards
def create_txt(dir_name):
    if dir_name[-1] != '/':
        dir_name += '/'

    if not os.path.isdir(dir_name):
        return
    
    # Get the list of files in the directory
    files = sorted(os.listdir(dir_name), key=extract_sort_key)
    
    with open(dir_name + 'board_states.txt', 'w') as f:
        prev_filename = files[0]
        wait = False
        cnt = 0
        for filename in files[1:]:
            if filename.endswith('box.jpg'):
                continue

            img_path = dir_name + filename
            if wait:
                cnt += 1
                if cnt > 8:
                    wait = False
                    cnt = 0
            # if board border is present, and a piece just spawned, save the previous image
            # also check for ctwc 2023 stats screen, do not save the stats screen
            elif compare_borders(img_path) and get_center_region(img_path) and is_no_yellow_line(img_path):
                f.write(prev_filename + '\n')
                wait = True

            prev_filename = filename
    
    print("File list created successfully.")

if __name__ == '__main__':
    dir_name = sys.argv[1]
    create_txt(dir_name)
