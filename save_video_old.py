import os
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
# from moviepy.video.io.concatenate_videoclips import concatenate_videoclips
from moviepy.editor import VideoFileClip, concatenate_videoclips

temp_folder = "D:\\downloads\\projects\\data\\temp"

if not os.path.exists(temp_folder):
    os.makedirs(temp_folder)

video_parts = []

# Extract the base URL and file names from the given URLs
base_url = "https://static.maestro.io/6388d822732876002fa33b7a/63d6cc457c7e5a307a9e5faa/"
start_num = 1682

i = start_num
while True:
    # filename = f"1080p_{i:03d}.ts"
    filename = f"1080p_{i}.ts"
    filepath = os.path.join(temp_folder, filename)
    if os.path.exists(filepath):
        video_parts.append(VideoFileClip(filepath))
        print(f"{filename} already exists, adding it to the list of video parts...")
        i += 1
        continue
    # url = f"{base_url}1080p_{i:03d}.ts"
    url = f"{base_url}1080p_{i}.ts"
    response = requests.get(url)
    if response.status_code != 200:
        break
    with open(filepath, "wb") as f:
        f.write(response.content)
    video_parts.append(VideoFileClip(filepath))
    print(f"Downloaded {filename} and added it to the list of video parts...")
    i += 1

from moviepy.editor import VideoFileClip, concatenate_videoclips

def stitch_videos(input_folder, output_file):
    clips = []
    for f in sorted(os.listdir(input_folder)):
        if f.endswith(".ts"):
            clips.append(VideoFileClip(f"{input_folder}/{f}"))
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, preset="ultrafast")

stitch_videos("/temp", "output.mp4")
