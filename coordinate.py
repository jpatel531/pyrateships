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

	def result_of_shot(self, player, opponent):
		return (player in self.assailants) and ('H' if opponent in self.ship_commanders() else 'M')

	def has_ship(self, player):
		return (player in self.ship_commanders()) and 'S'

	def render(self, viewer, opponent, stance):
		(subject, obj) = (opponent, viewer) if stance is 'defending' else (viewer, opponent)
		mark = (self.result_of_shot(subject, obj) or self.has_ship(viewer)) if stance is 'defending' else self.result_of_shot(subject, obj)
		return mark or '-'