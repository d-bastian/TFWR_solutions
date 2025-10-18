ws = get_world_size()

def setup_farm():
	clear()
	for x in range(ws):
		for y in range(ws):
			if get_ground_type() != Grounds.Soil:
				till()
			move(North)
		move(East)

def check_water():
	if num_items(Items.Water) > 0 and get_water() < 0.65:
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
	
def quick_sort(arr):
	if len(arr) <= 1:
		return arr
	
	pv = arr[len(arr) // 2]
	left = []
	middle = []
	right = []
	
	i = 0
	while i < len(arr):
		if arr[i][0] > pv[0]:
			left.append(arr[i])
		elif arr[i][0] == pv[0]:
			middle.append(arr[i])
		else:
			right.append(arr[i])
		i += 1
	
	return quick_sort(left) + middle + quick_sort(right)
