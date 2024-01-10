# Import necessary modules
import sys
from pytube import YouTube

# Function to extract YouTube video ID from URL
def get_video_id(url):
    yt = YouTube(url)
    return yt.video_id

# Function to process command line argument and output 
def main():
    # Get URL from command line arguments
    url = sys.argv[1]
    video_id = get_video_id(url)
    # Strip any leading or trailing white spaces (including newlines) before printing
    print(video_id.strip())

# Condition checking if this is the main script being executed
if __name__ == "__main__":
    main()