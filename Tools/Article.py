from bs4 import BeautifulSoup # Untuk menampilkan hanya content html saja
from rake_nltk import Rake # Keyword extraction
from Core.Database import Database
from Tools.TagDropper import TagDropper # Hapus beberapa tag dalam artikel

class Article:
	'''
		Class ini akan bertanggung jawab dengan text yang ada dalam artikel
	'''

	def __init__(self, title, body, file_name = '', table_name=''):
		self.title = title 
		self.body = body
		self.keyword = [] # ini adalah keyword yang akan digunakan sebagai link
		self.table_name = table_name # nama tabel untuk offline support

		self.conn = Database(file_name)

	'''
		Untuk mengekstrack keyword kita menggunakan rake
	'''
	def extract_keyword(self):

		# Menggunakan beautiful soup untuk mengambil text dari artikel
		clean = self.get_clean_body()

		# Dnegan rake kita ekstract keyword
		r = Rake(min_length=1, max_length=1)
		r.extract_keywords_from_text(clean)
		self.keyword = r.get_ranked_phrases()

		# Debug di terminal untuk melihat jumlah keyword
		print('Keyword extracted with ' + str(len(self.keyword)) + ' words')

	# Menggunakan beautiful soup untuk mengambil teks
	def get_clean_body(self):
		return BeautifulSoup(self.body, 'lxml').text

	'''
		Keyword yang ada akan di bandingkand engan judul artikel di wikipedia kemudian akan di beri link
	'''
	def get_wiki(self):
		key = []

		# File bisa didapat di kaggles
		file = open('titles.txt')
		for line in file:
			key.append(line[:-1].lower())
		file.close()

		for i in self.keyword :
			if i not in key:
				self.keyword.remove(i)

		for k in self.keyword :
			self.body = self.body.replace(' ' + k + ' ', ' <a href="https://en.wikipedia.org/wiki/'+ k +'">'+k+'</a> ')

	def get_keyword(self):
		return self.keyword

	def get_title(self):
		return self.title
		
	def get_content(self):
		return self.body

	def clean_html(self):

		# Drop tag yang menyusahkan dari web
		td = TagDropper(['img', 'h4', 'svg', 'a', 'figure', 'div', 'path'])
		td.feed(self.body)

		self.body = td.get_text()

	'''
		For Database
	'''
	def save_article(self):
		self.save(['title', 'raw_article'], (self.title, self.body))
		self.commit()

	def save(self, column, data):
		self.conn.insert(self.table_name, column, data)

	def commit(self):
		self.conn.commit()