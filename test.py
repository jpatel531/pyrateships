from base import Coordinate, Grid, Player, Ship

jamie, hamilton = Player.generate()

grid = Grid()

# print grid.render(jamie, 'attacking')
# print
# print

jamie.place_ship('A', (2, 2))

# print Coordinate.at_position(2, 2).ships

print 'Jamie looks at his board after placing a ship:'
print grid.render(jamie, 'defending')

print
print 'Hamilton looks at Jamie\'s board'

print grid.render(hamilton, 'attacking')

hamilton.hit(0, 0)

print 'Jamie looks at his board after Ham misses'
print grid.render(jamie, 'defending')
print 
print 'Ham looks at Jamie\'s board after he misses'
print grid.render(hamilton, 'attacking')

print
hamilton.hit(2, 2)

print 'Jamie looks at his board after Ham hits'
print grid.render(jamie, 'defending')
print 
print 'Ham looks at Jamies board after he hits'
print grid.render(hamilton, 'attacking')