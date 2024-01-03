import sqlite3
import sys

def run_query(database_path, query):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

def delete_all_videos(database_path):
    query = 'DELETE FROM Videos'
    run_query(database_path, query)

def main():
    database_path = '/Users/kamila/kidsvideos.db'
    delete_all_videos(database_path)
    print("All videos deleted successfully.")

if __name__ == "__main__":
    main()
