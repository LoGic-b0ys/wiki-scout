from Crawler import Crawler
from Article import Article


c = Crawler()

url = input()

c.set_url(url)
c.process()

a = Article(c.get_title(), c.get_content(), 'article.db', 'articles')
a.clean_html()
a.extract_keyword()
a.get_wiki()

a.save_article()

c.close()