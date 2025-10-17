ws = get_world_size()

def till_e():
	for x in range(get_world_size()):
		for y in range(get_world_size()):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)
def check_water():
	if num_items(Items.Water) > 0 and get_water() < 0.2:
		use_item(Items.Water)
		
def move_to(x ,y):
	while True:
		dx = get_pos_x()
		if dx < x:
			move(East)
		elif dx > x:
			move(West)
		if dx == x:
			break
	while True:
		dy = get_pos_y()
		if dy < y:
			move(North)
		elif dy > y:
			move(South)
		if dy == y:
			break

def get_pos():
	return get_pos_x(), get_pos_y()
	
def bubble_sort(list):
	n = len(list)
	for i in range(n):
		for j in range(0, n - i - 1):
			if list[j] < list[j + 1]:
				list[j], list[j + 1] = list[j + 1], list[j]
	return list