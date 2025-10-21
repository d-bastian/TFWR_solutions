from Util import *

while True:
	for x in range(ws):
		for y in range(ws):
			c_harvest()
			move(North)
			use_item(Items.Fertilizer)
		move(East)
	