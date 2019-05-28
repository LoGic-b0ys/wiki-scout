from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from Database import Database

db = Database('article.db')

row = db.read('articles', ['title'])

print(row)

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html', data_title = row)

Bootstrap(app)

app.run()