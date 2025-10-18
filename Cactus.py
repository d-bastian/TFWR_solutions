from Util import *

setup_farm()
change_hat(Hats.Wizard_Hat)

dirs = [North, East, South, West]

def sort_cactus():
	
	if measure() == None:
		return
		
	for dir in dirs:
		if measure(dir) == None:
			return
		
	for i in range(2):
		if measure() > measure(dirs[i]):
			swap(dirs[i])
		
while True:
	iter = 0
	while iter < ws**2:
		for x in range(ws):
			for y in range(ws):
				plant(Entities.Cactus)
				sort_cactus()
				move(North)
			move(East)
			iter += 1
	move_to(ws-1,ws-1)
	harvest()	 