from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from Database import Database

app = Flask(__name__)

@app.route('/')
def index():
	db = Database('article.db')
	row = db.read('articles', ['id', 'title'])
	return render_template('index.html', data_title = row)

@app.route('/article/<int:article_id>')
def article(article_id):
	db = Database('article.db')
	data = db.read('articles', ['title', 'raw_article'], ' WHERE id='+str(article_id))
	return render_template('article.html', article = data)

Bootstrap(app)

app.run()