class Coordinate(object):

	all = []

	@classmethod
	def at_position(klass, x, y):
		return [coordinate for coordinate in klass.all if (coordinate.x is x) and (coordinate.y is y)][0]

	def __init__(self, index):
		self.has_ship = False
		self.hit_attempted = False
		(self.x, self.y) = (index % 10, index / 10)
		self.all.append(self)

	def position(self): 
		return (self.x, self.y)

	def __repr__(self):
		if (self.hit_attempted): return 'X' if self.has_ship else 'O'
		else: return '-'