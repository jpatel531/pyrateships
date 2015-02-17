class Player(object):

	def __init__(self, name):
		self.name = name

	def hit(self, coordinate):
		coordinate.hit_attempted = True

	def place_ship(self, ship, coordinate):
		# coordinate.has_ship = True
		
