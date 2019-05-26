from Crawler import Crawler
from Article import Article


c = Crawler('article.db', 'articles')

c.set_url('https://fs.blog/2019/05/paragone/')
c.process()

a = Article(c.get_title(), c.get_content())
a.clean_html()
a.extract_keyword()
a.get_wiki()

print(a.get_content())

c.close()