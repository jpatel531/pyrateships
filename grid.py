from coordinate import Coordinate

class Grid(object):

	def __init__(self):
		for index in range(100): Coordinate(index)

	def __repr__(self): 
		return str(Coordinate.all)

	# def neighbouring_coordinates(self, coordinate, orientation):
