# Import necessary modules
import sqlite3
import sys

# Function to execute SQL queries on the SQLite database
def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()
    return cur.fetchall()

# Function to add video information into the Videos table in the database
def add_video(database_path, title, category, channel, youtubeID):
    # Check if a video with the same youtubeID already exists in the database
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

# Main function to test arguments and call appropriate logic
def main():
    # Check that all arguments are provided
    if len(sys.argv) != 5:
        print("Usage: python add_video.py <title> <category> <channel> <youtubeID>")
        sys.exit(1)

    # Extract command line arguments
    title = sys.argv[1]
    category = sys.argv[2]
    channel = sys.argv[3]
    youtubeID = sys.argv[4]

    # Check if any argument is missing
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

    # Specify the database path
    database_path = '/Users/kamila/kidyoutube/kidsvideos.db'

    # Call function to add video
    add_video(database_path, title, category, channel, youtubeID)
    print("Video added successfully.")

# Condition to check if this script is the main running script
if __name__ == "__main__":
    main()