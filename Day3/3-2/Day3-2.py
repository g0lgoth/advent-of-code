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

def movement(list1, list2):
	if (len(list1)) == (len(list2)):
		max = len(list1)
	elif len(list1)) > (len(list2)):
		max = len(list1)
	else :
		max = len(list2)
	for list_index in range max:
		list1[list_index]

## fonction qui permet de trier la commande pour chaque liste
## elle ressort en appelant d'autres fonctions une liste de vecteur de déplacement
def char_detection(list):
	list_index = 0 # je définie d'ou commence mon parcours de liste
	x, y = 0, 0
	map = [x, y]
	print(f"x {x} | y {y}")
	map_index = 0
	list_movement_map = [] # liste qui regroupe les vecteurs pour chaque déplacement
	for list_index in range (len(list)):
		if list[list_index][0] == "U" :
			map, x, y, map_index, list_movement_map = move_up(list, list_index, map, x, y, map_index, list_movement_map)
			map = [x, y]
			continue
		elif list[list_index][0] == "D" :
			map, x, y, map_index, list_movement_map = move_down(list, list_index, map, x, y, map_index, list_movement_map)
			map = [x, y]
			continue
		elif list[list_index][0] == "L" :
			map, x, y, map_index, list_movement_map = move_left(list, list_index, map, x, y, map_index, list_movement_map)
			map = [x, y]
			continue
		else :
			map, x, y, map_index, list_movement_map = move_right(list, list_index, map, x, y, map_index, list_movement_map)
			map = [x, y]
			continue
	return list_movement_map

def move_up(list, list_index, map, x, y, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		y = y+1
		map_index += 1
		map = [x, y]
		list_movement_map.append(map)
	return map, x, y, map_index, list_movement_map

def move_down(list, list_index, map, x, y, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		y = y-1
		map_index += 1
		map = [x, y]
		list_movement_map.append(map)
	return map, x, y, map_index, list_movement_map

def move_left(list, list_index, map, x, y, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		x = x-1
		map_index += 1
		map = [x, y]
		list_movement_map.append(map)
	return map, x, y, map_index, list_movement_map

def move_right(list, list_index, map, x, y, map_index, list_movement_map):
	cursor = 1
	distance_max = int(list[list_index][1:])
	for cursor in range (distance_max):
		x = x+1
		map_index += 1
		map = [x, y]
		list_movement_map.append(map)
	return map, x, y, map_index, list_movement_map

def cross_point(list1, list2):
	list_cross_point = []
	for list_index1 in range (len(list1)):
		for list_index2 in range (len(list2)):
			if list1[list_index1] == list2[list_index2]:
				list_cross_point.append(list1[list_index1])
			else :
				continue
	return list_cross_point

def absolute_value(list):
	for cursor in range (len(list)):
		list[cursor] = abs(list[cursor][0]) + abs(list[cursor][1])
	return list

def min_to_max_ladder(list):
	for cursor1 in range ((len(list))-1):
		for cursor2 in range ((len(list))-1):
			if list[cursor2] > list[(cursor2)+1]:
				temporary = list[(cursor2)+1]
				list[(cursor2)+1] = list[cursor2]
				list[cursor2] = temporary
			else :
				continue
	return list

## mise en forme du fichier txt
# file = "day3.txt"
file = "invention.txt"
# file = "invention1.txt"
# file = "test.txt"
# file = "test1.txt"
# file = "test2.txt"
list1, list2 = file_management(file)
print(f"--- list1 --- {list1} | --- list2 --- {list2}\n") # contrôle de la liste

## détection de l'indice par liste
list_movement_map1 = char_detection(list1)
list_movement_map2 = char_detection(list2)
list_cross_point = cross_point(list_movement_map1, list_movement_map2)
list_absolute_value = absolute_value(list_cross_point)
final_list = min_to_max_ladder(list_absolute_value)
print(f"final_list {final_list}")
print(f"\n--- The result is ---\n{final_list[0]}")