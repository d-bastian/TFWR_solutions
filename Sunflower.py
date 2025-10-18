from Util import *

setup_farm()
min_flower = 7
flowers = []

while True:
	for x in range(ws):
		for y in range(ws):
			plant(Entities.Sunflower)
			if get_entity_type() == Entities.Sunflower and measure() > min_flower:
				flowers.append((measure(), get_pos()))
			move(North)
			check_water()
		move(East)
	
	flowers = quick_sort(flowers)
	
	for _, cords in flowers:
		x, y = cords
		move_to(x, y)
		harvest()

	flowers = []