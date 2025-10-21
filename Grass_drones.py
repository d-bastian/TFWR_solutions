from Util import *
clear()

def drone_grass():
	while True:
		for y in range(ws):
			c_harvest()
			move(North)

while True:
	if spawn_drone(drone_grass):
		move(East)