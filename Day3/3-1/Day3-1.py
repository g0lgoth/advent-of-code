##  FUNCTIONS
def looking_for_opcode(list, index):
	if list[index] == 1:
		return index, 0
	elif list[index] == 2:
		return index, 1
	else:
		index += 1

def opcode_increment(index):
	starting_index = index+4
	return starting_index

def value_collecter(list, index):
	index_number1 = list[index+1]
	index_number2 = list[index+2]
	index_number3 = list[index+3]
	value1 = list[index_number1]
	value2 = list[index_number2]
	value3 = list[index_number3]
	return value1, value2, index_number3

def addition(value1, value2):
	new_value = value1 + value2
	return new_value
	
def multiplication(value1, value2):
	new_value = value1 * value2
	return new_value

def replace_index(list, value, index):
	list[index] = value
	return list

##  MAIN PROGRAM
initial_list = []
file = "day2.txt"
# file = "test.txt"
# file = "test1.txt"
# file = "test2.txt"
# file = "test3.txt"
# file = "test4.txt"
cursor = 0
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [int(initial_list[i]) for i in range (len(initial_list))]
initial_list = replace_index(initial_list, 12, 1)
initial_list = replace_index(initial_list, 2, 2)
# initial_list = replace_index(initial_list, 1, 1)
# initial_list = replace_index(initial_list, 1, 2)
# print(f"\n-- FIRST LIST --\ninitial_list: {initial_list}\n")
while initial_list[cursor] != 99:
	opcode_index, opcode_item = looking_for_opcode(initial_list, cursor)
	if opcode_item == 0 :
		cursor = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(initial_list, opcode_index)
		calcul_value = addition(index1, index2)
		initial_list = replace_index(initial_list, calcul_value, index_destination)
	else :
		cursor = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(initial_list, opcode_index)
		calcul_value = multiplication(index1, index2)
		initial_list = replace_index(initial_list, calcul_value, index_destination)
# new_list = list(initial_list)
# new_list = str(new_list)
# print(f"New list is:{new_list}")
# new_list = new_list.replace(" ","")
# new_list = new_list.replace("[","")
# new_list = new_list.replace("]","")
# print(f"New list is:{new_list}")
print(f"-- The final OPCODE --\n{initial_list}\n\nThe result is:\n{initial_list[0]}")