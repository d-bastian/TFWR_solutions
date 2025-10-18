from Util import *
change_hat(Hats.Purple_Hat)
clear()
till_e()

def plant_tree(x, y):
	if (x+y) % 2 == 0:
		plant(Entities.Tree)

while True:
	for x in range(ws):
		for y in range(ws):
			plant_tree(x, y)
			if can_harvest():
				harvest()
				plant_tree(x, y)
			move(North)
		move(East)