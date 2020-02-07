##  VARIABLES
initial_list = []
file = "test.txt"
initial_index = 0
cursor = 0

##  FUNCTIONS
def looking_for_opcode(list, index):
	if list[index] == 1:
		return index, false
	elif list[index] == 2:
		return index, true
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
	return value1, value2, value3

def addition(value1, value2):
	new_value = value1 + value2
	return new_value
	
def multiplication(value1, value2):
	new_value = value1 * value2
	return new_value

def replace_index(list, value, index):
	list[index] = value
	print(f"new value is: {list[index]}")

##  MAIN PROGRAM
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [int(initial_list[i]) for i in range (len(initial_list))]
print(f"List:\n{initial_list}\n")

while initial_list[cursor] != 99:
	opcode_index, opcode_item = looking_for_opcode(list_modify, initial_index)
	print(f"opcode_index, opcode_item {opcode_index} {opcode_item}")
	if opcode_item == false :
		new_opcode_index = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(list_modify, opcode_index)
		calcul_value = addition(index1, index2)
		list_modify = replace_index(list_modify, calcul_value, index_destination)
	else :
		new_opcode_index = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(list_modify, opcode_index)
		calcul_value = multiplication(index1, index2)
		list_modify = replace_index(list_modify, calcul_value, index_destination)
	cursor = new_opcode_index
	initial_list = list_modify

	
	
		