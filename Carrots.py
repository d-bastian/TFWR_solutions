from Util import *
change_hat(Hats.Purple_Hat)
setup_farm()

while True:
	for x in range(ws):
		for y in range(ws):
			c_harvest()
			plant(Entities.Carrot)
			move(North)
		move(East)