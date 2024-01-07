# Import necessary modules for Flask app
from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

# Initialize Flask app
app = Flask(__name__)

# Function to execute SQL queries in the SQLite database
def run_query(query, params=()):
  # Connect to the database and fetch all rows from executing the SQL query
  conn = sqlite3.connect('/Users/kamila/kidyoutube/kidsvideos.db')
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  return cur.fetchall()

# Define app route for home page
@app.route('/')
def home():
    # Fetch the latest 10 videos and all distinct channels, render the index page
    videos = run_query('SELECT * FROM Videos ORDER BY upload_date DESC LIMIT 12')
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    channels = [channel[0] for channel in channels]
    return render_template('index.html', videos=videos, channels=channels)

# Define app route for channels page, which returns JSON format channels
@app.route('/channels')
def channels():
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    return jsonify([channel[0] for channel in channels])

# Define route for a specific channel, with a default page number of 1 if not provided
@app.route('/channel/<channel>', defaults={'page': 1})
@app.route('/channel/<channel>/<int:page>')
def channel(channel, page):
    # Fetch videos from the specified channel and render them 
    offset = (page - 1) * 20
    videos = run_query('SELECT * FROM Videos WHERE channel = ? ORDER BY upload_date DESC LIMIT 20 OFFSET ?', (channel, offset))
    return render_template('channel.html', videos=videos, channel=channel, page=page)

# Define route for videos transmitted in JSON format
@app.route('/videos')
def videos():
    cur = run_query('SELECT * FROM Videos')
    videos = [dict(id=row[0], title=row[1], category=row[2], youtube_link=row[3], upload_date=row[4]) for row in cur]
    return jsonify(videos)
    
# Define route for video page
@app.route('/video/<int:id>')
def video(id):
    video = run_query('SELECT * FROM Videos WHERE id = ?', (id,))
    if video:
        video_id = video[0][3].split('watch?v=')[-1].split('/')[0]
        return render_template('video.html', title=video[0][1], category=video[0][2], video_id=video_id, upload_date=video[0][4])
    else:
        return 'Video not found'


# Define route for database display
@app.route('/database')
def database():
    videos = run_query('SELECT * FROM Videos')
    return render_template('database.html', videos=videos)

# Define app route for categories page, which returns JSON format categories
@app.route('/categories')
def categories():
    categories = run_query('SELECT DISTINCT category FROM Videos ORDER BY category')
    return jsonify([category[0] for category in categories])

# Define route for a specific category, with a default page number of 1 if not provided
@app.route('/category/<category>', defaults={'page': 1})
@app.route('/category/<category>/<int:page>')
def category(category, page):
    offset = (page - 1) * 20
    videos = run_query('SELECT * FROM Videos WHERE category = ? ORDER BY upload_date DESC LIMIT 20 OFFSET ?', (category, offset))
    return render_template('category.html', videos=videos, category=category, page=page)

# Define route for search function
@app.route('/search')
def search():
  search_term = request.args.get('q', '')
  query = 'SELECT * FROM Videos WHERE title LIKE ? LIMIT 10'
  results = run_query(query, ('%' + search_term + '%', ))
  return jsonify(results)

# Ensure the Flask app runs when this script is directly executed
if __name__ == '__main__':
    app.run(debug=True)