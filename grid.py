from coordinate import Coordinate

class Grid(object):

	def __init__(self):
		self.coordinates = [x[:] for x in [[Coordinate()]*10]*10]

	def __repr__(self):
		return str(self.cells)