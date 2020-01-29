# help(open)

#  VARIABLES
fuel_list=[]

#  FUNCTIONS
def calcul(number):
    result = (number//3)-2
    return result

# def increment_calcul(num):


# ALGO
# fuel_list = open("Day1.txt", "r").read()
with open("Day1.txt") as fuel_list:
    fuel_list = fuel_list.readlines()
    # fuel_list = [x.strip() for x in fuel_list]
    fuel_list = [x.rstrip() for x in fuel_list]
    fuel_list = [int(x) for x in fuel_list]
    # fuel_list = [int(x) and x.strip() for x in fuel_list]
print(fuel_list[0])
print(fuel_list)
result_test = calcul(fuel_list[0])
print(result_test)
final_result = [calcul(x) for x in fuel_list]
# for i in fuel_list:
#     final_result = calcul(fuel_list)
print(final_result)
# for i in fuel_list:
#     fuel_list = int(fuel_list[i])
# print(fuel_list)
# calcul = int(content[0])/3
# print(f"calcul is {calcul}")