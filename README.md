# Tetris Game Board Extractor

This repository generates JSON data containing Tetris game boards from the Classic Tetris World Championship (CTWC) 2023 games.

## Installation

1. Set up a virtual environment:
    ```bash
    python3 -m venv myenv
    . myenv/bin/activate
    ```

2. Install required packages:
    ```bash
    pip install yt-dlp opencv-python numpy scikit-image
    ```

## Usage

1. Download the CTWC 2023 video from YouTube using `yt-dlp`:
    ```bash
    yt-dlp <ctwc2023video>
    ```
   For example:
    ```bash
    yt-dlp https://youtu.be/ppOupG_aNBA?si=kbqonRSYMoKjwxWX
    ```
   Rename the downloaded video to something concise.

2. Extract Tetris game boards from the downloaded video:
    ```bash
    python convert_video_to_images.py <mp4_file>
    ```

3. Filter out unnecessary images and extract board states:
    ```bash
    python filter.py <dir_name>
    ```

4. Write the extracted board states to a JSON file:
    ```bash
    python write_boards_to_json.py <dir_name/board_states.txt>
    ```

5. Generate JSON of all Tetris game boards:
    ```bash
    python create_all_boards_json.py
    ```
