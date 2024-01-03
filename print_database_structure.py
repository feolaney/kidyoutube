import sqlite3

# Connect to the sqlite database
conn = sqlite3.connect('/Users/kamila/kidyoutube/kidsvideos.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the query to get all tables in the database 
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch all the tables
tables = cursor.fetchall()

for table in tables:
    # For each table, execute a SELECT SQL command to get the structure
    cursor.execute(f'PRAGMA table_info({table[0]})')

    # Fetch all rows as a list and print
    columns = cursor.fetchall()
    print(f"Table: {table[0]}")
    for column in columns:
        print(column)

# Close the connection to the database
conn.close()
