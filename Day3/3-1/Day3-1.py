##  FUNCTIONS

## Fonction qui permet de mettre en forme le fichier texte de l'épreuve du jour
## Cette fonction reçoit un fichier et en ressort 2 listes
def file_management(file):
	initial_list = []
	initial_list = open(file,"r") # mise en forme de la liste de travail initiale
	initial_list = initial_list.read() # mise en forme de la liste de travail initiale
	print(f"--- initial_list ---\n{initial_list}\n") # contrôle de la liste
	list = initial_list.split("\n")
	list1 = list[0].split(",") # mise en forme de la liste de travail initiale
	list2 = list[1].split(",") # mise en forme de la liste de travail initiale
	print(f"list1 {list1} | list1[0] {list1[0]}")
	print(f"list2 {list2} | list2[0] {list2[0]}")
	return list1, list2

## fonction qui permet de trier la commande pour chaque liste
## elle ressort en appelant d'autres fonctions une liste de vecteur de déplacement
def char_detection(list):
	list_index = 0 # je définie d'ou commence mon parcours de liste
	x, y = 0, 0
	print(f"x {x} | y {y}")
	map_index = 0
	list_movement_map = [] # liste qui regroupe les vecteurs pour chaque déplacement
	for list_index in range (len(list)):
		map = [x, y]
		if list[list_index][0] == "U" :
			map_index, list_movement_map = move_up(list, list_index, y, map_index, list_movement_map)
			# continue
		elif list[list_index][0] == "D" :
			map_index, list_movement_map = move_down(list, list_index, y, map_index, list_movement_map)
			continue
		elif list[list_index][0] == "L" :
			x, map_index, list_movement_map = move_left(list, list_index, x, map_index, list_movement_map)
			continue
		else :
			map_index, list_movement_map = move_right(list, list_index, x, map_index, list_movement_map)
			# continue
	return list_movement_map

def move_up(list, list_index, map, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		map = [map[0], (map[1] + 1)]
		map_index += 1
		list_movement_map.append(map)
	return map, map_index, list_movement_map

def move_down(list, list_index, map, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		map = [map[0], (map[1] - 1)]
		map_index += 1
		list_movement_map.append(map)
	return map, map_index, list_movement_map

def move_left(list, list_index, x, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		# print(f"cursor {cursor}\n")
		x = x -1
		print(f"x {x}\n")
		map_index += 1
		# print(f"map_index {map_index}\n")
		list_movement_map.append(map)
	return x, map_index, list_movement_map

def move_right(list, list_index, map, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		map = [(map[1]+1), map[1]]
		map_index += 1
		list_movement_map.append(map)
	return map, map_index, list_movement_map

def cross_point(list1, list2):
	list_cross_point = []
	for list_index1 in range (len(list1)):
		for list_index2 in range (len(list2)):
			if list1[list_index1] == list2[list_index2]:
				list_cross_point.append(list1[list_index1])
			else :
				continue
	return list_cross_point

## mise en forme du fichier txt
# file = "day3.txt"
file = "invention.txt"
# file = "test.txt"
# file = "test1.txt"
# file = "test2.txt"
list1, list2 = file_management(file)
print(f"--- list1 --- {list1} | --- list2 --- {list2}\n") # contrôle de la liste

## détection de l'indice par liste
list_movement_map1 = char_detection(list1)
# print(f"list_movement_map1 {list_movement_map1}\n") # contrôle de la liste
list_movement_map2 = char_detection(list2)
print(f"list_movement_map2 {list_movement_map2}\n") # contrôle de la liste
# list_cross_point = cross_point(list_movement_map1, list_movement_map2)
print(f"\nlist_cross_point {list_cross_point}\n") # contrôle de la liste

# nothing_to_use = map_table.append(map) # ajout dans la liste du premier vecteur 
# map_table_cursor = 0
# file_cursor = 0 # it is where I am on my list. I have to cover all items on my list
# cursor_check = 0 # 
# manhattan_distance_table = [] # liste qui garde les valeurs absolues de x et y pour ensuite trier la plus basse

# list1 = file_management(initial_list)
# for file_cursor in range (len(initial_list)):
	# map = (x,y)
	# if initial_list[file_cursor][0] == "U" :
		# map, map_table_cursor, map_table, x, y = move_up(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	# elif initial_list[file_cursor][0] == "D" :
		# map, map_table_cursor, map_table, x, y = move_down(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	# elif initial_list[file_cursor][0] == "L" :
		# map, map_table_cursor, map_table, x, y = move_left(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
	# else :
		# map, map_table_cursor, map_table, x, y = move_right(initial_list, file_cursor, map, map_table_cursor, map_table, x, y)
# print(f"file_cursor {file_cursor+1}") # je dois ajouter 1 car dans la liste on part de 0 jusqu'à 6
# print(f"map_table_cursor {map_table_cursor}")
# print(f"liste de tous les vecteurs map | map_table {map_table}")
# cursor_check = calcul_cursor(cursor_check, initial_list)
# scan_cursor = 0
# similar_vector_table = [] # liste qui balaie les vecteur similaires et qui les stocke
# for scan_cursor in range (len(map_table)):
	# for scan_cursor1 in range (len(map_table)):
		# if scan_cursor == scan_cursor1:
			# continue
		# else :
			# if map_table[scan_cursor] == map_table[scan_cursor1]:
				# if map_table[scan_cursor] == (999, 999) :
					# continue
				# else :
					# nothing_to_use = similar_vector_table.append(map_table[scan_cursor])
					# map_table[scan_cursor1] = 999, 999
					# map_table[scan_cursor] = 999, 999
			# else :
				# continue
# print(f"\nliste des vecteurs similaires venant de la liste des vecteurs cartes | similar_vector_table {similar_vector_table}")
# print(f"liste de tous les vecteurs map | map_table {map_table}\n")
# scan_final = 0
# for scan_final in range (len(similar_vector_table)):
	# x, y = similar_vector_table[scan_final]
	# result = abs(x) + abs(y)
	# nothing_to_use = manhattan_distance_table.append(result)
# print(f"liste des vecteurs de distance | manhattan_distance_table {manhattan_distance_table}\n")
# try :
	# i = 0
	# while i == (len(manhattan_distance_table)):
		# manhattan_distance_table = [manhattan_distance_table[scan_final] > manhattan_distance_table[scan_final+1] for scan_final in range (len(manhattan_distance_table-1))]
		# i += 1
		# print(f"manhattan_distance_table[0] {manhattan_distance_table[0]}")
# except :
	# print(f"manhattan_distance_table | La distance minimale est: {manhattan_distance_table[0]}")