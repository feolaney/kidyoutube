from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

def run_query(query, params=()):
  conn = sqlite3.connect('/Users/kamila/kidyoutube/kidsvideos.db')
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  return cur.fetchall()

@app.route('/')
def home():
    videos = run_query('SELECT * FROM Videos ORDER BY upload_date DESC LIMIT 10')
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    channels = [channel[0] for channel in channels]
    return render_template('index.html', videos=videos, channels=channels)

@app.route('/channels')
def channels():
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    return jsonify([channel[0] for channel in channels])

@app.route('/channel/<channel>', defaults={'page': 1})
@app.route('/channel/<channel>/<int:page>')
def channel(channel, page):
    # rest of your function
    offset = (page - 1) * 20
    videos = run_query('SELECT * FROM Videos WHERE channel = ? ORDER BY upload_date DESC LIMIT 20 OFFSET ?', (channel, offset))
    return render_template('channel.html', videos=videos, channel=channel, page=page)

@app.route('/videos')
def videos():
    cur = run_query('SELECT * FROM Videos')
    videos = [dict(id=row[0], title=row[1], category=row[2], youtube_link=row[3], upload_date=row[4]) for row in cur]
    return jsonify(videos)

@app.route('/video/<int:id>')
def video(id):
  video = run_query('SELECT * FROM Videos WHERE id = ?', (id,))
  if video:
    video_id = video[0][3].split('watch?v=')[-1].split('/')[0]
    return render_template('video.html', title=video[0][1], category=video[0][2], video_id=video_id, upload_date=video[0][4])
  else:
    return 'Video not found'

@app.route('/database')
def database():
    videos = run_query('SELECT * FROM Videos')
    return render_template('database.html', videos=videos)

@app.route('/categories')
def categories():
    categories = run_query('SELECT DISTINCT category FROM Videos ORDER BY category')
    return jsonify([category[0] for category in categories])

@app.route('/category/<category>', defaults={'page': 1})
@app.route('/category/<category>/<int:page>')
def category(category, page):
    offset = (page - 1) * 20
    videos = run_query('SELECT * FROM Videos WHERE category = ? ORDER BY upload_date DESC LIMIT 20 OFFSET ?', (category, offset))
    return render_template('category.html', videos=videos, category=category, page=page)

@app.route('/search')
def search():
  search_term = request.args.get('q', '')
  # Execute search query with a wildcard match.
  query = 'SELECT * FROM Videos WHERE title LIKE ? LIMIT 10'
  # '%' is a wildcard symbol matching any number of characters, 
  # putting it at the beginning and end of search_term will match titles containing search_term anywhere.
  results = run_query(query, ('%' + search_term + '%', ))
  # Send results back as JSON
  return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)