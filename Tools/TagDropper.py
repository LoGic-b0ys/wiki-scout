from html.parser import HTMLParser

class TagDropper(HTMLParser):
	def __init__(self, tags_to_drop, *args, **kwargs):
		HTMLParser.__init__(self, *args, **kwargs)
		self._text = []
		self._tags_to_drop = set(tags_to_drop)

	def clear_text(self):
		self._text = []

	def get_text(self):
		return ''.join(self._text)

	def handle_starttag(self, tag, attrs):
		if tag not in self._tags_to_drop:
			self._text.append(self.get_starttag_text())

	def handle_endtag(self, tag):
		self._text.append('</{0}>'.format(tag))

	def handle_data(self, data):
		self._text.append(data)