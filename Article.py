from bs4 import BeautifulSoup
from rake_nltk import Rake
from Database import Database
from TagDropper import TagDropper

class Article:

	def __init__(self, title, body):
		self.title = title
		self.body = body
		self.keyword = []

		self.db = Database('article.db')

	def extract_keyword(self):
		clean = self.get_clean_body()
		r = Rake(min_length=1, max_length=1)
		r.extract_keywords_from_text(clean)
		self.keyword = r.get_ranked_phrases()
		print('Keyword extracted with ' + str(len(self.keyword)) + ' words')

	def get_clean_body(self):
		return BeautifulSoup(self.body, 'lxml').text

	def get_wiki(self):
		key = []
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

	def get_content(self):
		return self.body

	def clean_html(self):
		td = TagDropper(['img', 'h4', 'svg', 'a', 'figure', 'div', 'path'])
		td.feed(self.body)

		self.body = td.get_text()