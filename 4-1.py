##  FUNCTIONS
def direction(list, file_cursor, map, map_table, map_table_cursor):
	if list[file_cursor][0] == "U" :
		move_up(list, file_cursor, map, map_table, map_table_cursor)
	elif list[file_cursor][0] == "D" :
		move_down(list, file_cursor, map, map_table, map_table_cursor)
	elif list[file_cursor][0] == "L" :
		move_left(list, file_cursor, map, map_table, map_table_cursor)
	else :
		move_right(list, file_cursor, map, map_table, map_table_cursor)

def move_up(list, file_cursor, map, map_table, map_table_cursor):
	i = 1
	movement = int(list[file_cursor][1:])
	for i in range (movement):
		print(f"{type(map)}")
		print(f"{map[0]} {map[1]}")
		map = map[1]+i
		print(f"{map[0]} {map[1]}")
		print(f"map {map}")
		print(f"{type(map)}")
		map_table = map_table.append(map)
		map_table_cursor += 1
	return map, map_table_cursor

# def move_down(list, file_cursor, map, map_table, map_table_cursor):
	# i = 1
	# movement = int(list[file_cursor][1:])
	# for i in range (movement):
		# map = map[1]-i
		# map_table_cursor += 1
		# map_table = open("map_table.txt","w+")
		# map_table = map_table[map_table_cursor].write(map)
		# map_table.close()
	# return map, map_table_cursor

# def move_right(list, file_cursor, map, map_table, map_table_cursor):
	# i = 1
	# movement = int(list[file_cursor][1:])
	# for i in range (movement):
		# map = map[0]+i
		# map_table_cursor += 1
		# map_table = open("map_table.txt","w+")
		# map_table = map_table[map_table_cursor].write(map)
		# map_table.close()
	# return map, map_table_cursor

# def move_left(list, file_cursor, map, map_table, map_table_cursor):
	# i = 1
	# movement = int(list[file_cursor][1:])
	# for i in range (movement):
		# map = map[0]-i
		# map_table_cursor += 1
		# map_table = open("map_table.txt","w+")
		# map_table = map_table[map_table_cursor].write(map)
		# map_table.close()
	# return map, map_table_cursor

##  MAIN PROGRAM
# file = "day3.txt"
# file = "test.txt"
file = "invention.txt"
# file = "test1.txt"
# file = "test2.txt"
# file = "test3.txt"
# file = "test4.txt"
map = [0,0] # this is my plan. I will add movement on him
file_cursor = 0 # it is where I am on my list. I have to cover all items on my list
map_table_cursor = 0
map_table = list()
print(f"map_table: {map_table}")
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [initial_list[i] for i in range (len(initial_list))]
print(f"-- FIRST LIST --\ninitial_list: {initial_list}")
print(f"initial_list[0][0]: {initial_list[0][0]}")
print(f"initial_list[0][1:]: {initial_list[0][1:]}")
for file_cursor in range (len(initial_list)):
	map, map_table_cursor = direction(initial_list, file_cursor, map, map_table, map_table_cursor)
	printf(f"map: {map}")