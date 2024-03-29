# Import necessary modules
import sys
import sqlite3
from googleapiclient.discovery import build
from google_API_key import get_google_api_key

# Initialize YouTube Data API
api_key = get_google_api_key()
youtube = build('youtube', 'v3', developerKey=api_key)

# Continue with the rest of your script...

# Function to run SQL queries
def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    return cur.fetchall()

# Function to add video details to database
def add_video(database_path, title, category, youtubeID, channel):
    # Check if a video with the same youtubeID already exists
    result = run_query(database_path, 'SELECT * FROM Videos WHERE youtubeID = ?', (youtubeID,))
    if result:
        return
    youtube_link = "https://www.youtube.com/watch?v=" + youtubeID
    query = 'INSERT INTO Videos (title, category, youtube_link, upload_date, channel, youtubeID) VALUES (?, ?, ?, datetime(\'now\'), ?, ?)'
    run_query(database_path, query, (title, category, youtube_link, channel, youtubeID))

# Function to get videos from YouTube playlist
def get_playlist_videos(playlist_id):
    request = youtube.playlistItems().list(
        part='contentDetails',
        playlistId=playlist_id,
        maxResults=200
    )
    video_ids = []
    while request is not None:
        response = request.execute()
        video_ids.extend([item['contentDetails']['videoId'] for item in response['items']])
        request = youtube.playlistItems().list_next(request, response)
    return video_ids

# Function to get video details
def get_video_info(video_id):
    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()
    items = response.get('items', [])
    if items:
        snippet = items[0]['snippet']
        return {
            'title': snippet['title'],
            'channel': snippet['channelTitle']
        }
    return None

# Main function to handle command line arguments and add videos to database from playlist
def main():
    if len(sys.argv) < 3:
        print("Usage: python script.py playlist_id category")
        sys.exit(1)

    playlist_id = sys.argv[1]
    category = sys.argv[2]
    video_ids = get_playlist_videos(playlist_id)

    database_path = '/Users/Shared/.kidyoutube/kidsvideos.db'

    for video_id in video_ids:
        info = get_video_info(video_id)
        if info is not None:
            add_video(database_path, info['title'], category, video_id, info['channel'])

# Condition to check if this is the main script being executed
if __name__ == '__main__':
    main()