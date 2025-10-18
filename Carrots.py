from Util import *
change_hat(Hats.Purple_Hat)
clear()
till_e()

while True:
	for x in range(ws):
		for y in range(ws):
			plant(Entities.Carrot)
			if can_harvest():
				harvest()
				plant(Entities.Carrot)
			move(North)
		move(East)