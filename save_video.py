import os
import requests
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.editor import VideoFileClip, concatenate_videoclips
import tqdm

TEMP_FOLDER = "D:\\downloads\\projects\\data\\temp"
BASE_URL = "https://static.maestro.io/6388d822732876002fa33b7a/63d6cc457c7e5a307a9e5faa/"
START_NUM = 1

def download_video_parts():
    if not os.path.exists(TEMP_FOLDER):
        os.makedirs(TEMP_FOLDER)
    video_parts = []
    i = START_NUM

    while True:
        filename = f"1080p_{i}.ts" # the filename format to add to base url
        filepath = os.path.join(TEMP_FOLDER, filename)
        if os.path.exists(filepath):
            video_parts.append(VideoFileClip(filepath))
            print(f"{filename} already exists, adding it to the list of video parts...")
            i += 1
            continue
        url = f"{BASE_URL}1080p_{i}.ts"
        response = requests.get(url)
        if response.status_code != 200:
            break
        with open(filepath, "wb") as f:
            f.write(response.content)
        video_parts.append(VideoFileClip(filepath))
        print(f"Downloaded {filename} and added it to the list of video parts...")
        i += 1

'''
TODO: this method adds all the clips to the memory then stitches it together
its a terrible idea for large videos, and currently does not work for my use case
need to do a better job.
'''
def stitch_videos(input_folder, output_file):
    clips = []
    for f in tqdm.tqdm(sorted(os.listdir(input_folder))):
        if f.endswith(".ts"):
            clips.append(VideoFileClip(f"{input_folder}/{f}"))
    final_clip = concatenate_videoclips(clips)
    final_clip.write_videofile(output_file, codec="mpeg4", preset="slow",progress_bar=True)

if __name__ == "__main__":
    download_video_parts()
    stitch_videos(TEMP_FOLDER, "output.mp4")
