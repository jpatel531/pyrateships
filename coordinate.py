class Coordinate(object):

	all = []

	@classmethod
	def at_position(klass, x, y):
		return next(coordinate for coordinate in klass.all if (coordinate.x is x) and (coordinate.y is y))

	def __init__(self, index):
		self.assailants, self.ships = [], []
		(self.x, self.y) = (index % 10, index / 10)
		self.all.append(self)

	def ship_commanders(self): 
		return map(lambda ship: ship.commander, self.ships)		

	def has_missed(self, player):
		return (player in self.assailants) and (player.opponent not in self.ship_commanders())

	def has_hit(self, player):
		return (player in self.assailants) and (player.opponent in self.ship_commanders())

	def has_ship(self, player):
		return (player in self.ship_commanders())

	def render(self, viewer, stance):
		subject = viewer.opponent if stance is 'defending' else viewer
		if (self.has_missed(subject)): return 'M'
		if (self.has_hit(subject)): return 'H'
		if stance is 'defending' and self.has_ship(viewer) : return 'S'
		return '-'