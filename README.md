# Tetris Game Board Extractor

This repository extracts Tetris game boards found in Classic Tetris World Championship (CTWC) videos, found on YouTube, to a JSON file. Works on videos from 2020-2023 in the 1v1 format.  

## Usage

- In the terminal, execute the script `run.sh` with a YouTube link to a Classic Tetris World Championship (CTWC) video as the argument.
  
    ```bash
    ./run.sh <ctwc_youtube_link> <year>
    ```
    For example:
    ```bash
    ./run.sh https://youtu.be/ppOupG_aNBA?si=kbqonRSYMoKjwxWX 2023
    ```

- Once the script has finished running, the file `all_boards.json` will contain board states from all games found in the provided video

- Each time the script is run, it will append to `all_boards.json` without overwriting existing data.

## Known Issues

Some extracted boards are not valid Tetris boards. Depending on the video link, sometimes the CTWC organizers reuse the board border outside of tetris play. For example, in the 2020 finals, they have a countdown before games using the border. As well as 2023, there is a stats page using the border (this one is fixed in most cases, only gets one wrong frame). Thus, a small minority of the data is invalid noise, this will hopefully be fixed later on.