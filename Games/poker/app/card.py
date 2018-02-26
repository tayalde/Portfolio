class Card(object):
	def __init__(self, value, suite):
		self.value = value
		self.suite = suite

	def __str__(self):
		return str(self.__dict__)

	def __repr__(self):
		return '<Card: {}-{}>'.format(self.value, self.suite)

	def __eq__(self, other):
		return self.__dict__ == other.__dict__
