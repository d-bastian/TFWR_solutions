from Util import *

dirs = [West,South,East,North]
clear()
dir=0

while True:
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, ws**2)
	while get_entity_type() != Entities.Treasure:
		dir = (dir + 2 * move(dirs[dir]) - 1) % 4
	harvest()