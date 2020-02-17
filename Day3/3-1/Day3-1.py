##  FUNCTIONS

def move_up(initial_list, file_cursor, map, map_table_cursor, map_table, x, y):
	i = 1
	movement = int(initial_list[file_cursor][1:])
	for i in range (movement):
		y = y+1
		map = (x,y)
		nothing_to_use = map_table.append(map)
		map_table_cursor += 1
	return map, map_table_cursor, map_table, x, y

def move_down(initial_list, file_cursor, map, map_table_cursor, map_table, x, y):
	i = 1
	movement = int(initial_list[file_cursor][1:])
	for i in range (movement):
		y = y-1
		map = (x,y)
		nothing_to_use = map_table.append(map)
		map_table_cursor += 1
	return map, map_table_cursor, map_table, x, y

def move_left(initial_list, file_cursor, map, map_table_cursor, map_table, x, y):
	i = 1
	movement = int(initial_list[file_cursor][1:])
	for i in range (movement):
		x = x-1
		map = (x,y)
		nothing_to_use = map_table.append(map)
		map_table_cursor += 1
	return map, map_table_cursor, map_table, x, y

def move_right(initial_list, file_cursor, map, map_table_cursor, map_table, x, y):
	i = 1
	movement = int(initial_list[file_cursor][1:])
	for i in range (movement):
		x = x+1
		map = (x,y)
		nothing_to_use = map_table.append(map)
		map_table_cursor += 1
	return map, map_table_cursor, map_table, x, y

# def scan_list():
	

##  MAIN PROGRAM
# file = "day3.txt"
file = "invention.txt"
# file = "test.txt"
# file = "test1.txt"
# file = "test2.txt"
# file = "test3.txt"
# file = "test4.txt"
x, y = 0, 0
map = (x,y) # this is my plan. I will add movement on him
file_cursor = 0 # it is where I am on my list. I have to cover all items on my list
map_table_cursor = 0
scan_cursor = 0
map_table = []
similar_vector_table = []
manhattan_distance_table = []
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [initial_list[i] for i in range (len(initial_list))]
nothing_to_use = map_table.append(map)
for file_cursor in range (len(initial_list)):
	map = (x,y)
	if initial_list[file_cursor][0] == "U" :
		map, map_table_cursor, map_table, x, y = move_up(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	elif initial_list[file_cursor][0] == "D" :
		map, map_table_cursor, map_table, x, y = move_down(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	elif initial_list[file_cursor][0] == "L" :
		map, map_table_cursor, map_table, x, y = move_left(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	else :
		map, map_table_cursor, map_table, x, y = move_right(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
print(f"file_cursor {file_cursor}")
print(f"map_table_cursor {map_table_cursor}")
print(f"map_table {map_table}")
for scan_cursor in range (len(map_table)):
	for scan_cursor2 in range (len(map_table)):
		if scan_cursor2 == scan_cursor:
			continue
		else :
			if map_table[scan_cursor] == map_table[scan_cursor2]:
				print(f"scan_cursor {scan_cursor}")
				nothing_to_use2 = similar_vector_table.append(map_table[scan_cursor])
				map_table[scan_cursor2] = 999
			else :
				continue
print(f"\nsimilar_vector_table {similar_vector_table}\n")
for scan_final in range (len(similar_vector_table)):
	x, y = similar_vector_table[scan_final]
	result = abs(x) + abs(y)
	manhattan_distance_table = manhattan_distance_table.append(result)
for scan_final in range (len(manhattan_distance_table-1)):
	if manhattan_distance_table[scan_final] > manhattan_distance_table[scan_final+1]:
		flash_variable = manhattan_distance_table[scan_final]
		manhattan_distance_table[scan_final+1] = manhattan_distance_table[scan_final]
		manhattan_distance_table[scan_final] = flash_variable
		