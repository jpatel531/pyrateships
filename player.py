from coordinate import Coordinate
from ship import Ship

class Player(object):

	@classmethod
	def generate(klass, name1='Jamie', name2='Hamilton'):
		players = (player1, player2) = (klass(name1), klass(name2))
		player1.opponent, player2.opponent = player2, player1
		return players

	def __init__(self, name):
		self.name = name
		self.ships = Ship.generate_all(commander=self)

	def hit(self, x,y):
		Coordinate.at_position(x,y).assailants.append(self)

	def place_ship(self, ship_name, (x, y), orientation='horizontal'):
		ship = self.ships.pop(self.ships.index(next(ship for ship in self.ships if ship.name is ship_name)))
		for unit in range(ship.length):
			position = (x + unit, y) if orientation is 'horizontal' else (x, y + unit)
			Coordinate.at_position(*position).ships.append(ship)