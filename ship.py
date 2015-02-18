class Ship(object):

	@classmethod
	def generate_all(klass, commander):
		return map(lambda name: klass(name, commander), ['A', 'B', 'C', 'D', 'E'])

	def __init__(self, name, commander):
		self.name, self.commander = name, commander
		if name is "A": self.length = 5
		if name is "B": self.length = 4
		if name is "C" or name is "D": self.length = 3
		if name is "E": self.length = 2 