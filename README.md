`python3 -m venv myenv`
`. myenv/bin/activate`

`pip install yt-dlp opencv-python numpy scikit-image`
`yt-dlp <ctwc2023video>`
for example
`yt-dlp https://youtu.be/ppOupG_aNBA?si=kbqonRSYMoKjwxWX`

rename downloaded video to something concise

first `python convert_video_to_images.py mp4_file` (from ctwc2023)
second `python filter.py dir_name` (for both board dirs)
third `python write_boards_to_json.py dir_name/board_states.txt` (for both board txt in dir)
fourth `python create_all_boards_json.py`