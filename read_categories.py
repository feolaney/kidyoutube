import sqlite3

def run_query(database_path, query):
    conn = sqlite3.connect(database_path)
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def get_categories(database_path):
    query = 'SELECT DISTINCT category FROM Videos'
    categories = run_query(database_path, query)
    # Unpack categories from list of tuples to list
    categories = [category for (category,) in categories]
    return categories

def main():
    database_path = '/Users/kamila/Kids Youtube Videos/kidsvideos.db'
    categories = get_categories(database_path)
    for category in categories:
        print(category)

if __name__ == "__main__":
    main()
