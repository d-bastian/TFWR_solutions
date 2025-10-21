from Util import *

def tree():
	for y in range(ws-1):
		check_water()
		c_harvest()
		if y%2 == 0:
			plant(Entities.Tree)
		else:
			plant(Entities.Bush)
		move(North)

while True:
	if spawn_drone(tree):
		move(North)
		move(East)
		