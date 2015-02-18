class Coordinate(object):

	all = []

	@classmethod
	def at_position(klass, x, y):
		return next(coordinate for coordinate in klass.all if (coordinate.x is x) and (coordinate.y is y))

	def __init__(self, index):
		self.assailants = []
		self.ships = []
		(self.x, self.y) = (index % 10, index / 10)
		self.all.append(self)

	# def __repr__(self):
	# 	if (self.hit_attempted): return 'X' if self.has_ship else 'O'
	# 	else: return '-'

	# def render(self):
	# 	