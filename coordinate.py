class Coordinate(object):

	def __init__(self):
		self.has_ship = False
		self.hit_attempted = False

	def __repr__(self):
		if (self.hit_attempted):
			return 'X' if self.has_ship else 'O'
		else:
			return '-'