# Tetris Game Board Extractor

This repository generates JSON data containing Tetris game boards from the Classic Tetris World Championship (CTWC) games. (only tested on 2023 so far)  

## Usage

1. In the terminal, run the following
    ```bash
    ./run.sh <ctwc_youtube_link>
    ```
   For example:
    ```bash
    ./run.sh https://youtu.be/ppOupG_aNBA?si=kbqonRSYMoKjwxWX
    ```

2. Once the script has finished running, all_boards.json will contain board states from all games found in the video

3. Each run of the script will append to all_boards.json, not overwrite it