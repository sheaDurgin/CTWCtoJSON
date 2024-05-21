# Tetris Game Board Extractor

This repository extracts Tetris game boards found in Classic Tetris World Championship (CTWC) videos, found on YouTube, to a JSON file. (only tested on 2023 games so far)  

## Usage

- In the terminal, execute the script `run.sh` with a YouTube link to a Classic Tetris World Championship (CTWC) video as the argument.
  
    ```bash
    ./run.sh <ctwc_youtube_link>
    ```
    For example:
    ```bash
    ./run.sh https://youtu.be/ppOupG_aNBA?si=kbqonRSYMoKjwxWX
    ```

- Once the script has finished running, the file `all_boards.json` will contain board states from all games found in the provided video

- Each time the script is run, it will append to `all_boards.json` without overwriting existing data.