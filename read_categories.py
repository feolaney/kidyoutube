# Import sqlite3 module to interact with SQLite database
import sqlite3

# The run_query function takes as arguments a path to the database file and an SQL query string
# Opens a connection to the SQLite database file and returns all rows from executing the SQL query
def run_query(database_path, query):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

# Function to get all unique categories in the Videos database, ordered by their latest upload date
def get_categories(database_path):
    query = 'SELECT category FROM Videos GROUP BY category ORDER BY MAX(upload_date) DESC'
    categories = run_query(database_path, query)
    # List comprehension to unpack categories from tuples to a list
    categories = [category[0] for category in categories]
    return categories

# Main function to test the get_categories function
def main():
    database_path = '/Users/Shared/.kidyoutube/kidsvideos.db'
    categories = get_categories(database_path)
    # Print categories
    for category in categories:
        print(category)

# Ensures the main function only runs when this file is being run directly
if __name__ == "__main__":
    main()