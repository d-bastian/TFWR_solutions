from Util import *
setup_farm()

min_flower = 7
list = []

while True:
	for x in range(ws):
		for y in range(ws):
			plant(Entities.Sunflower)
			if get_entity_type() == Entities.Sunflower and measure() > min_flower:
				list.append((measure(),get_pos()))
			move(North)
			check_water()
		move(East)
	list = bubble_sort(list)
	for _, cords in list:
		x, y = cords
		move_to(x,y)
		harvest()

	list = []