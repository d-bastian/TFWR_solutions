from Util import *

def sunflower():
	for y in range(ws):
		if get_ground_type() != Grounds.Soil:
			till()
		check_water()
		c_harvest()
		plant(Entities.Sunflower)
		move(North)

while True:
	if spawn_drone(sunflower):
		move(East)