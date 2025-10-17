clear()
change_hat(Hats.Brown_Hat)

ws = get_world_size()

while True:
	for x in range(ws):
		for y in range(ws):
			if can_harvest():
				harvest()
			move(North)
		move(East)