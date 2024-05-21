import cv2
import os
import sys

# LEFT BOARD
board_y1 = 156 # 158
board_y2 = 615 # 614
board_x1 = 402 # 405
board_x2 = 634 # 632

# RIGHT BOARD
RIGHT_OFFSET = 244
right_board_x1 = RIGHT_OFFSET + board_x1
right_board_x2 = RIGHT_OFFSET + board_x2

def write_frame(frame, frame_number, output_folder, suffix, y1, y2, x1, x2):
    cropped_frame = frame[y1:y2, x1:x2]
    board_filename = os.path.join(output_folder, f"{frame_number:04d}_{suffix}.jpg")
    cv2.imwrite(board_filename, cropped_frame)

# crop frame for video to where board should be and save it as a jpg
def extract_frames(video_path, output_folder1, output_folder2):
    if not os.path.exists(output_folder1):
        os.makedirs(output_folder1)

    if not os.path.exists(output_folder2):
        os.makedirs(output_folder2)

    video_capture = cv2.VideoCapture(video_path)

    if not video_capture.isOpened():
        print("Error: Could not open video.")
        return
    
    frame_number = 0

    while True:
        ret, frame = video_capture.read()

        if not ret:
            break

        write_frame(frame, frame_number, output_folder1, 'board', board_y1, board_y2, board_x1, board_x2)
        write_frame(frame, frame_number, output_folder2, 'board', board_y1, board_y2, right_board_x1, right_board_x2)

        frame_number += 1
        
    video_capture.release()
    print(f"Extracted {frame_number} frames to '{output_folder1} and {output_folder2}'.")

def convert_video_to_images(video_path):
    boards_dir_name = 'boards/'

    if not os.path.exists(boards_dir_name):
        os.makedirs(boards_dir_name)

    output_folder1 = f"{boards_dir_name}board1-{video_path.split('/')[-1].split('.')[0]}/"
    output_folder2 = f"{boards_dir_name}board2-{video_path.split('/')[-1].split('.')[0]}/"
    extract_frames(video_path, output_folder1, output_folder2)

    return output_folder1, output_folder2

if __name__ == '__main__':
    video_path = sys.argv[1]

    convert_video_to_images(video_path)
