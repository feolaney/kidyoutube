import sys
from pytube import YouTube

def get_video_id(url):
    yt = YouTube(url)
    return yt.video_id

# Get URL from command line arguments
url = sys.argv[1]
video_id = get_video_id(url)
# Strip any leading or trailing white spaces (including newlines) before printing
print(video_id.strip())  