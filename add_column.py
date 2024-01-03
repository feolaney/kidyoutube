import sqlite3
import sys

def run_query(database_path, query):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query)
    conn.commit()

def add_column(database_path, column_name, data_type):
    query = f'ALTER TABLE Videos ADD COLUMN {column_name} {data_type}'
    run_query(database_path, query)

def main():
    database_path = '/Users/kamila/kidsvideos.db'  # Provided path to the SQLite database
    add_column(database_path, 'channel', 'TEXT')
    add_column(database_path, 'youtubeID', 'TEXT')
    print("Columns added successfully.")

if __name__ == "__main__":
    main()
