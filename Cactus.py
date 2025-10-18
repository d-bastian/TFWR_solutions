from Util import *

change_hat(Hats.Wizard_Hat)
clear()
till_e()

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
	harvest()

		
		 