from coordinate import Coordinate
from copy import copy

class Grid(object):

	def __init__(self):
		for index in range(100): Coordinate(index)

	def render(self, viewer, stance):
		return [coordinate.render(viewer, stance) for coordinate in Coordinate.all]