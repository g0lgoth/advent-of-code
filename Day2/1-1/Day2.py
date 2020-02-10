##  VARIABLES
initial_list = []
list_modify = []
file = "test.txt"
initial_index = 0
cursor = 0

##  FUNCTIONS
def looking_for_opcode(list, index):
	if list[index] == 1:
		print(f"List index:\n{index}\n")
		return index, 0
	elif list[index] == 2:
		print(f"List:\n{list[index]}\n")
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
	print(f"value collecter:\n{index_number1}")
	print(f"value collecter:\n{index_number2}")
	print(f"value collecter:\n{index_number3}")
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
	print(f"new value is: {list[index]} | {index} | {list}")
	list[index] = value
	return list[index]

##  MAIN PROGRAM
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [int(initial_list[i]) for i in range (len(initial_list))]
list_modify = initial_list
print(f"initial_list:\n{initial_list}\n")
print(f"list_modify:\n{list_modify}\n")
print(f"List cursor 0:\n{initial_list[0]}\n")

while initial_list[cursor] != 99:
	opcode_index, opcode_item = looking_for_opcode(list_modify, initial_index)
	print(f"opcode_index {opcode_index} | opcode_item {opcode_item}")
	if opcode_item == 0 :
		new_opcode_index = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(list_modify, opcode_index)
		print(f"index1 {index1} | index2 {index2} | index_destination {index_destination}")
		calcul_value = addition(index1, index2)
		print(f"calcul_value {calcul_value}\n")
		list_modify = replace_index(list_modify, calcul_value, index_destination)
	else :
		new_opcode_index = opcode_increment(opcode_index)
		index1, index2, index_destination = value_collecter(list_modify, opcode_index)
		calcul_value = multiplication(index1, index2)
		list_modify = replace_index(list_modify, calcul_value, index_destination)
	cursor = new_opcode_index
	initial_list = list_modify
	print(f"list_modify {list_modify}\n")
	print(f"initial_list {initial_list}\n")
	
	
		