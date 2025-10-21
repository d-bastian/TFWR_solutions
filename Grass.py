from Util import *

clear()
change_hat(Hats.Straw_Hat)

while True:
	for x in range(ws):
		for y in range(ws):
			c_harvest()
			move(North)
		move(East)