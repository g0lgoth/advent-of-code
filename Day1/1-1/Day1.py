#  VARIABLES
fuel_list = []
final_result = 0

#  FUNCTIONS
def calcul(number):
    result = (number//3)-2
    return result

# def increment_calcul(num):

# ALGO
# fuel_list = open("Day1.txt", "r").read()
with open("Day1.txt") as fuel_list:
    fuel_list = fuel_list.readlines()
    fuel_list = [x.rstrip("\n") for x in fuel_list]
    fuel_list = [int(x) for x in fuel_list]
print(fuel_list)
fuel_list = [calcul(x) for x in fuel_list]
print(fuel_list)
print(len(fuel_list))
for i in range (0, len(fuel_list)):
    final_result += fuel_list[i]
    print(final_result)
print(final_result)
