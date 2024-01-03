from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3

app = Flask(__name__)

def run_query(query, params=()):
  conn = sqlite3.connect('/Users/kamila/Kids Youtube Videos/kidsvideos.db')
  cur = conn.cursor()
  cur.execute(query, params)
  conn.commit()
  return cur.fetchall()

@app.route('/')
def home():
    videos = run_query('SELECT * FROM Videos ORDER BY upload_date DESC LIMIT 10')
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    channels = [channel[0] for channel in channels]
    return render_template('index.html', videos=videos, channels=channels) # pass channels to template

@app.route('/channels')
def channels():
    channels = run_query('SELECT DISTINCT channel FROM Videos ORDER BY channel')
    return jsonify([channel[0] for channel in channels])

@app.route('/channel/<channel>')
def channel(channel):
    videos = run_query('SELECT * FROM Videos WHERE channel = ? ORDER BY channel', (channel,))
    return render_template('channel.html', videos=videos, channel=channel)

@app.route('/admin4994', methods=['GET', 'POST'])
def admin():
  if request.method == 'POST':
    title = request.form['title']
    category = request.form['category']
    youtube_link = request.form['youtube_link']
    # If "https://youtube.com" is in the URL, replace it with "https://www.youtube.com"
    youtube_link = youtube_link.replace("https://youtube.com", "https://www.youtube.com")
    # If "https://m.youtube.com/" is in the URL, replace it with "https://www.youtube.com/"
    youtube_link = youtube_link.replace("https://m.youtube.com/", "https://www.youtube.com/")
    # If "si=" exists and "v=" comes after "si=", remove everything from "si=" onward
    # If "v=" exists and "si=" comes after "v=", remove everything from "si=" onwards
    if "si=" in youtube_link and "v=" in youtube_link:
        si_index = youtube_link.index("si=")
        v_index = youtube_link.index("v=")
        if si_index < v_index:
            youtube_link = youtube_link[:si_index] + youtube_link[v_index:]
        else:
            youtube_link = youtube_link[:si_index]
    # If "&feature=" exists then delete "&feature=" and any text after it
    if "&feature=" in youtube_link:
        youtube_link = youtube_link.split("&feature=")[0]
    # If the URL ends with "&", remove the "&"
    if youtube_link.endswith("&"):
        youtube_link = youtube_link[:-1]
    # Insert video data into the database
    run_query('INSERT INTO Videos (title, category, youtube_link) VALUES (?, ?, ?)', (title, category, 
youtube_link))

    return redirect(url_for('home'))
  return """
    <h1>Add new Video</h1>
    <form method='post'>
      Title: <input type='text' name='title'><br>
      Category: <input type='text' name='category'><br>
      Channel: <input type='text' name='channel'><br>
      Youtube Link: <input type='text' name='youtube_link'><br>
      <input type='submit' value='Add video'>
    </form>
  """

@app.route('/videos')
def videos():
  cur = run_query('SELECT * FROM Videos')
  videos = [dict(id=row[0], title=row[1], category=row[2], youtube_link=row[3], upload_date=row[4]) for 
row in cur.fetchall()]
  return jsonify(videos)

@app.route('/video/<int:id>')
def video(id):
  video = run_query('SELECT * FROM Videos WHERE id = ?', (id,))
  if video:
    video_id = video[0][3].split('watch?v=')[-1].split('/')[0]
    return render_template('video.html', title=video[0][1], category=video[0][2], video_id=video_id, 
upload_date=video[0][4])
  else:
    return 'Video not found'

@app.route('/database')
def database():
  videos = run_query('SELECT * FROM Videos')
  output = ''
  for video in videos:
      output += f"""
      <h2>{video[1]}</h2>
      <p>Category: {video[2]}</p>
      <p>Channel: {video[5]}</p>
      <p>YouTube Link: {video[3]}</p>
      <p>Upload Date: {video[4]}</p>
      <hr>
      """
  return output

@app.route('/categories')
def categories():
    categories = run_query('SELECT DISTINCT category FROM Videos ORDER BY category')
    return jsonify([category[0] for category in categories])

@app.route('/category/<category>')
def category(category):
    videos = run_query('SELECT * FROM Videos WHERE category = ? ORDER BY category', (category,))
    return render_template('category.html', videos=videos, category=category)

if __name__ == '__main__':
    app.run(debug=True)
