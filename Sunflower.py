from Util import *
clear()
till_e()
min_flower = 7
list = []

while True:
	for x in range(ws):
		for y in range(ws):
			plant(Entities.Sunflower)
			if get_entity_type() == Entities.Sunflower and measure() > 7:
				list.append((measure(),get_pos()))
			move(North)
			check_water()
		move(East)
	list = bubble_sort(list)
	for pedals, cords in list:
		x, y = cords
		move_to(x,y)
		harvest()

	list = []