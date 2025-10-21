from Util import *

def carrot():
	for y in range(ws):
		if get_ground_type() != Grounds.Soil:
			till()
		c_harvest()
		check_water()
		plant(Entities.Carrot)
		move(North)


while True:
	if spawn_drone(carrot):
		move(East)