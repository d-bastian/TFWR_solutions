from Util import *

while True:
	for x in range(ws):
		for y in range(ws):
			if can_harvest():
				harvest()
			move(North)
			use_item(Items.Fertilizer)
		move(East)
		use_item(Items.Fertilizer)
	