from Web.app import WebApp

app = WebApp('article.db')

app.get_app().run()