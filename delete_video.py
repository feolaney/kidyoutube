import sqlite3
import sys

def run_query(database_path, query, params=()):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query, params)
    conn.commit()

def delete_video(database_path, title):
    query = 'DELETE FROM Videos WHERE title = ?'
    run_query(database_path, query, (title, ))

def main():
    if len(sys.argv) != 2:
        print("Usage: python delete_video.py <title>")
        sys.exit(1)

    title = sys.argv[1]
    database_path = '/Users/kamila/kidyoutube/kidsvideos.db'
    delete_video(database_path, title)
    print(f"Video with title '{title}' deleted successfully.")

if __name__ == "__main__":
    main()
