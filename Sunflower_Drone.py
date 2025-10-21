from Util import *

setup_farm()

def sunflower():
	for y in range(ws):
		check_water()
		c_harvest()
		plant(Entities.Sunflower)
		move(North)

while True:
	if spawn_drone(sunflower):
		move(East)