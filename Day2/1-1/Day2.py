##  VARIABLES
initial_list = []
file = "test.txt"
i = 0

initial_list = open(file,"r")
initial_list = initial_list.read()
initial_list = initial_list.split(",")
initial_list = [int(initial_list[i]) for i in range (len(initial_list))]
print(f"List:\n{initial_list}\n")
a = initial_list[2]
b = initial_list[3]
c = a + b
print(f"Calcul:\n{c}\n")
