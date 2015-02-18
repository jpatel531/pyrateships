from coordinate import Coordinate
from copy import copy

class Grid(object):

	def __init__(self):
		for index in range(100): Coordinate(index)

	def render(self, viewer, stance):

		view = copy(Coordinate.all)

		for index, coordinate in enumerate(view):
			# print coordinate
			ship_commanders = map(lambda ship: ship.commander, coordinate.ships)
			view[index] = '-'
			if stance is 'attacking':
				if viewer in coordinate.assailants:
					view[index] = 'M'
					if len(coordinate.ships) > 0 and viewer not in ship_commanders: view[index] = 'H'
			elif stance is 'defending':
				if len(coordinate.ships) > 0:
					if viewer in ship_commanders: view[index] = 'S'
					if len(coordinate.assailants) > 0 and viewer not in coordinate.assailants:
						view[index] = 'H'
				else:
					if len(coordinate.assailants) > 0 and viewer not in coordinate.assailants: view[index] = 'M'
		
		return view