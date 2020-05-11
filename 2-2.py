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

def intcode_program(initial_list, cursor):
	# print(f"cursor {cursor}")
	while initial_list[cursor] != 99:
		# print(f"cursor {cursor}")
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
	return initial_list

def comparison(intcode_value):
	if intcode_value == 19690720:
		return True
	else:
		return False

def increment_noun(verb_status, initial_list, noun):
	if noun >= 99 :
		noun = 99
		return initial_list, noun
	else :
		if verb_status == True :
			noun += 1
			initial_list = replace_index(initial_list, noun, 1)
			return initial_list, noun
		else :
			initial_list = replace_index(initial_list, noun, 1)
			return initial_list, noun

def increment_verb(initial_list, verb):
	if verb > 99 :
		verb = 0
		initial_list = replace_index(initial_list, verb, 2)
		return initial_list, True, verb
	else :
		verb += 1
		initial_list = replace_index(initial_list, verb, 2)
		return initial_list, False, verb


##  MAIN PROGRAM
initial_list = []
file = "day2.txt"
# file = "test.txt"
# file = "test1.txt"
# file = "test2.txt"
# file = "test3.txt"
# file = "test4.txt"
cursor = 0
noun = 0
verb = 0
status = False
intcode_status = False
initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [int(initial_list[i]) for i in range (len(initial_list))]
print(f"\n-- FIRST LIST --\ninitial_list: {initial_list}\n")

while intcode_status != True:
	new_initial_list = list(initial_list)
	# print(f"new_initial_list {new_initial_list}")
	new_initial_list, verb_status, verb = increment_verb(new_initial_list, verb)
	new_initial_list, noun = increment_noun(verb_status, new_initial_list, noun)
	intcode_list = intcode_program(new_initial_list, cursor)
	# print(f"intcode_list {intcode_list}")
	intcode_value = intcode_list[0]
	intcode_status = comparison(intcode_value)
	print(f"intcode_value {intcode_value} | noun {noun} | verb {verb}")
print(f"\nThe good value is:\nnoun: {noun} | verb: {verb}")
final_value = noun * 100 + verb
print(f"\nThe good value is:\n{final_value}")