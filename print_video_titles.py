import sqlite3

def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    return rows

def get_videos(database_path):
    # Fetch title, youtubeID, category from Videos ordered by category and upload_date in descending order
    query = 'SELECT title, youtubeID, category FROM Videos ORDER BY category, upload_date DESC'
    videos = run_query(database_path, query)
    return videos

def main():
    database_path = '/Users/kamila/Kids Youtube Videos/kidsvideos.db'
    videos = get_videos(database_path)
    current_category = ''
    for video in videos:
        title, youtubeID, category = video
        if category != current_category:
            print('\nCategory: {}\n'.format(category))
            current_category = category
        print("Title: {}, YoutubeID: {}".format(title, youtubeID))

if __name__ == "__main__":
    main()
