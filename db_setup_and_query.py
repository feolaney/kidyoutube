# Import necessary modules
import sqlite3
import os

# Define function to run queries
def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    rows = cur.fetchall()
    return rows

# Function to retrieve the videos from database
def get_videos(database_path):
    query = 'SELECT title, youtubeID, category FROM Videos ORDER BY category, upload_date DESC'
    videos = run_query(database_path, query)
    return videos

# Function to print the structure of database tables
def print_table_structure(database_path):
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        cursor.execute(f'PRAGMA table_info({table[0]})')
        columns = cursor.fetchall()
        print(f"Table: {table[0]}")
        for column in columns:
            print(column)

    conn.close()

def main():
    # Path to the SQLite database
    database_path = '/Users/kamila/kidyoutube/kidsvideos.db'

    # If the database does not exist, create it and set up the Videos table
    if not os.path.exists(database_path):
        conn = sqlite3.connect(database_path)
        cursor = conn.cursor()
        cursor.execute('''
           CREATE TABLE IF NOT EXISTS Videos(
           id INTEGER PRIMARY KEY,
           title TEXT NOT NULL,
           category TEXT NOT NULL,
           youtube_link TEXT NOT NULL,
           upload_date DATE DEFAULT (datetime('now','localtime')),
           channel TEXT,
           youtubeID TEXT);
        ''')
        conn.commit()
        print("Database has been created.")
    else:
        # If it does exist, provide options to display database structure and contents
        print("Database already exists.")
        
        user_input = input("Would you like a report of the database structure? [y/n]: ")
        if user_input.lower() == "y":
            print_table_structure(database_path)

        user_input = input("Would you like a report of the database contents? [y/n]: ")
        if user_input.lower() == "y":
            print("\n---\n")
            videos = get_videos(database_path)
            current_category = ''
            for video in videos:
                title, youtubeID, category = video
                if category != current_category:
                    print('\nCategory: {}\n'.format(category))
                    current_category = category
                print("Title: {}, YoutubeID: {}".format(title, youtubeID))

# Condition checking if this is the main script being executed
if __name__ == "__main__":
    main()