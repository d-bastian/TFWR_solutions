from Util import *

setup_farm()

def check():
	move_to(0,0)
	start = measure()
	move_to(ws-1, ws-1)
	end = measure()
	if start == end:
		harvest()

while True:
	for x in range(ws):
		for y in range(ws):
			plant(Entities.Pumpkin)
			if get_entity_type() == Entities.Dead_Pumpkin:
				use_item(Items.Weird_Substance)
				plant(Entities.Pumpkin)
			move(North)
			check_water()
		move(East)
	check()
	