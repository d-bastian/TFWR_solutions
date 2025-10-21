from Util import *

setup_farm()
change_hat(Hats.Purple_Hat)

def plant_tree(x, y):
	if (x+y) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Bush)

while True:
	for x in range(ws):
		for y in range(ws):
			c_harvest()
			plant_tree(x, y)
			move(North)
		move(East)