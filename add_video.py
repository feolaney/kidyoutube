import sqlite3
import sys

def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    return cur.fetchall()

def add_video(database_path, title, category, channel, youtubeID):
    # Check if a video with the same youtubeID already exists
    query = 'SELECT * FROM Videos WHERE youtubeID = ?'
    result = run_query(database_path, query, (youtubeID,))
    if result:
        print("Error: A video with this youtubeID already exists in the database.")
        return
    # Construct the standard YouTube watch URL
    url = "https://www.youtube.com/watch?v=" + youtubeID
    # Insert video data into the database
    query = 'INSERT INTO Videos (title, category, youtube_link, channel, youtubeID) VALUES (?, ?, ?, ?, ?)'
    run_query(database_path, query, (title, category, url, channel, youtubeID))

def main():
    # Check that all arguments are passed
    if len(sys.argv) != 5:
        print("Usage: python add_video.py <title> <category> <channel> <youtubeID>")
        sys.exit(1)

    # extracting command line arguments
    title = sys.argv[1]
    category = sys.argv[2]
    channel = sys.argv[3]
    youtubeID = sys.argv[4]

    # checking if any argument is missing
    if not title:
        print("Missing parameter: title")
        sys.exit(1)
    if not category:
        print("Missing parameter: category")
        sys.exit(1)
    if not channel:
        print("Missing parameter: channel")
        sys.exit(1)
    if not youtubeID:
        print("Missing parameter: youtubeID")
        sys.exit(1)

    database_path = '/Users/kamila/kidyoutube/kidsvideos.db'

    add_video(database_path, title, category, channel, youtubeID)
    print("Video added successfully.")

if __name__ == "__main__":
    main()
