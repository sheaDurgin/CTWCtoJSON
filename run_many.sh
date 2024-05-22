#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <txt_with_video_year_pairs>"
    echo "Example file structure: 
    https://youtu.be/9penfXgG96g?si=UZoZNQJxvZ-Amktl 2023
    https://youtu.be/xYiDMKf8X0s?si=GZ13B4QInRQ2ibL3 2023"
    exit 1
fi

INPUT_FILE="$1"

while IFS= read -r line; do
    if [ -n "$line" ]; then
        YOUTUBE_LINK=$(echo "$line" | awk '{print $1}')
        YEAR=$(echo "$line" | awk '{print $2}')
        ./run.sh "$YOUTUBE_LINK" "$YEAR"
    fi
done < "$INPUT_FILE"
