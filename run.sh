#!/bin/bash

if [ "$#" -ne 2 ]; then
	echo "Usage: $0 <ctwc_youtube_link> <year>"
	exit 1
fi

# virtual environment
python3 -m venv myenv
. myenv/bin/activate

# install dependencies
pip install yt-dlp opencv-python numpy scikit-image

# download directory
VIDEO_DIR="./videos"
mkdir -p "$VIDEO_DIR"

YOUTUBE_LINK="$1"

# download video
yt-dlp -o "$VIDEO_DIR/%(title)s.%(ext)s" "$YOUTUBE_LINK"

# get path of the video
VIDEO_PATH=$(ls -t "$VIDEO_DIR" | head -n 1)
VIDEO_PATH="$VIDEO_DIR/$VIDEO_PATH"

BOARDS_DIR="./boards"
mkdir -p "$BOARDS_DIR"

YEAR="$2"

# run python script to write/append all_boards.json
python scripts/run.py "$VIDEO_PATH" "$YEAR" "$BOARDS_DIR"

if [ -d "$VIDEO_DIR" ]; then
	# Remove the directory and its contents
	rm -r "$VIDEO_DIR"
	echo "'$VIDEO_DIR' and its contents successfully removed."
fi

if [ -d "$BOARDS_DIR" ]; then
	# Remove the directory and its contents
	rm -r "$BOARDS_DIR"
	echo "'$BOARDS_DIR' and its contents successfully removed."
fi