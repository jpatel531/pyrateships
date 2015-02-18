from coordinate import Coordinate

class Player(object):

	def __init__(self, name):
		self.name = name

	def hit(self, (x,y)):
		Coordinate.at_position(x, y).hit_attempted = True

	def place_ship(self, ship, (x, y), orientation='horizontal'):
		for unit in range(ship.length):
			position = (x + unit, y) if orientation is 'horizontal' else (x, y + unit)
			Coordinate.at_position(*position).has_ship = True