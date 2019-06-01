# This is the library we use
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


'''
	This class provide interface to the crawler with selenium and chromedriver

	Role of this class is a crawler so you can implement this if you want to crawl the web
'''
class Crawler:

	'''
		This class construct with 2 argument.

		file_name is a string that indicates where you want to put your crawl result in a database.
		url is a string where is your review
	'''
	def __init__(self) :
		# We use chrome web driver
		webdriver_path = './chromedriver'

		# This is our browsing option
		chrome_options = Options()
		chrome_options.add_argument('--headless') # We don't browse with a window
		chrome_options.add_argument('--window-size=1920x1080') # And UltraHD screen size
		self.browser = webdriver.Chrome(executable_path=webdriver_path, options=chrome_options)
		self.title = ''
		self.body = ''
		self.url = ''

	'''
		This method provide an interface to change the URL and automatically change the anime id too
	'''
	def set_url(self, url):
		self.url = url


	'''
		This is our main crawl process. After the preparation is complete we can execute this to crawl the web
	'''
	def process(self):
		# Open the url
		self.browser.get(self.url)

		'''
			You can change this to your preferred review container
		'''
		container_div = self.browser.find_element_by_class_name("entry-content")
		self.title = self.browser.find_element_by_class_name("entry-title").text

		self.body = container_div.get_attribute('innerHTML')

		# print('Process complete')


	'''
		Ini adalah class untuk mengambil feed dari farnam street
	'''
	def get_feed(self):
		self.browser.get(self.url)

		titles = self.browser.find_elements_by_css_selector(".entry-title > a")

		res = {}
		for x in titles :
			res[x.text] = x.get_attribute('href')

		return res


	'''
		This method provide an content and title
	'''
	def get_content(self):
		return self.body

	def get_title(self):
		return self.title

	def close(self):
		self.browser.close()