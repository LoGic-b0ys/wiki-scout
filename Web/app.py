from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from Core.Database import Database
from Core.Crawler import Crawler
from Tools.Article import Article

class WebApp:

	'''
		Ini adalah class yang bertanggung jawab dengan backend dan frontend web yang ada
	'''
	def __init__(self, db_name):
		app = Flask(__name__)

		# Rute pertama adalah offline article
		@app.route('/')
		def index():
			db = Database(db_name)
			row = db.read('articles', ['id', 'title'])
			return render_template('index.html', data_title = row)

		@app.route('/article/<int:article_id>')
		def article(article_id):
			db = Database(db_name)
			data = db.read('articles', ['title', 'raw_article'], ' WHERE id='+str(article_id))
			return render_template('article.html', article = data)

		@app.route('/input')
		def input():
			article_data = {}
			return render_template('url.html', data=article_data)

		@app.route('/url', methods = ['POST', 'GET'])
		def url():

			'''
				Ini adalah untuk memroses URL yang dimasukkan. Proses yang dilakukan adalah :
				1. Crawl artikelnya
				2. Ambil teksnya saja
				3. Ekstrak keyword
				4. Clean HTMl nya dari image dan tag lain
				5. Berikan link pada text
			'''
			article_data = {}
			c = Crawler()
			if request.method == 'POST':
				c.set_url('https://fs.blog/'+ request.form['url'])
			if request.method == 'GET':
				c.set_url(request.args.get('farnam'))
			c.process()

			# Ini masuk pemrosesan artikel
			a = Article(c.get_title(), c.get_content(), db_name, 'articles')
			a.extract_keyword()
			a.clean_html()
			a.get_wiki()

			# Penyimpanan artikel
			a.save_article()
			article_data = {
				'title': a.get_title(),
				'content': a.get_content()
			}
			return render_template('url.html', data = article_data)

		# Route ini untuk feed dari artikel terbaru farnam street
		@app.route('/feed/<int:page>')
		def feed(page):
			c = Crawler()
			c.set_url('https://fs.blog/blog/page/' + str(page))
			db = Database(db_name)

			# Ini method untuk mengambil artikel paling paru
			titles = c.get_feed()

			# Pengecekan apakah ada artikel yang sudah disimpan
			# Karena ketika artikel sudah disimpan, maka link akan mengarah ke web seite tersimpan saja
			title_status = {}
			for title in titles.keys() :
				data = db.read('articles', ['id', 'title'], ' WHERE title="'+title+'"')
				if len(data) > 0 :
					title_status[title] = data[0][0]
				else :
					title_status[title] = titles[title]

			return render_template('feed.html', titles = titles, title_status = title_status, page=page)

		Bootstrap(app)

		self.webapp = app

	def get_app(self):
		return self.webapp