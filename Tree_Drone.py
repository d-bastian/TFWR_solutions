from Util import *
setup_farm()

def tree():
	for y in range(ws-1):
		check_water()
		if y%2 == 0:
			plant(Entities.Tree)
			
		else:
			plant(Entities.Bush)
		if can_harvest():
			harvest()
			check_water()
			if y%2 == 0:
				plant(Entities.Tree)
				
			else:
				plant(Entities.Bush)
		move(North)

while True:
	if spawn_drone(tree):
		move(North)
		move(East)
		