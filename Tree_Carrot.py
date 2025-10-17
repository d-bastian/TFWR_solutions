from Util import *
change_hat(Hats.Purple_Hat)
clear()
till_e()

def plant_tree_carrot(x, y):
	if (x+y) % 2 == 0:
		plant(Entities.Tree)
	else:
		plant(Entities.Carrot)
	check_water()

while True:
	for x in range(ws):
		for y in range(ws):
			plant_tree_carrot(x, y)
			if can_harvest():
				harvest()
				plant_tree_carrot(x, y)
			move(North)
		move(East)