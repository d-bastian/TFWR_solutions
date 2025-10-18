from Util import *
clear()

def drone_grass():
	while True:
		for y in range(ws):
			if can_harvest():
				harvest()
			move(North)

while True:
	for i in range(max_drones()+1):
		move_to(i, 0)
		spawn_drone(drone_grass)