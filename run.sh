#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <youtube_link>"
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

# run python script to write/append all_boards.json
python scripts/run.py "$VIDEO_PATH"
