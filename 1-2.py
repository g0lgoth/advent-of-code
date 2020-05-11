##  VARIABLES
sum_of_fuel = []
final_result = 0

##  FUNCTIONS
def simple_calcul(number):
    result = (number//3)-2
    return result

def sum_of_element(list):
	sum_result = 0
	# print(f"\nThe lenght of the list is: {len(list)}\n")
	for i in range (len(list)):
		sum_result += list[i]
		# print(f"result: {sum_result} / Iteration: {i}")
	return sum_result

# def zero_tracking(list_element, iteration):
    # list_element = simple_calcul(list_element)
    # result = list_element
    # z = 1
    # print(f"test{iteration} / iteration n°{z} / calculation number {list_element} / result is {result}\n")
    # while simple_calcul(list_element) > 0 :
        # z += 1
        # list_element = simple_calcul(list_element)
        # result += list_element
        # print(f"test{iteration} / iteration n°{z} / calculation number {list_element} / result is {result}\n")
    # return result

def zero_tracking(list_element):
    list_element = simple_calcul(list_element)
    result = list_element
    while simple_calcul(list_element) > 0 :
        list_element = simple_calcul(list_element)
        result += list_element
    return result

## Start of the program

## I open the file which containt some integers in strings
## I put them on a list, I transform them to be ready for calculation
with open("Day1.txt") as sum_of_fuel:
    sum_of_fuel = sum_of_fuel.readlines()
    sum_of_fuel = [x.rstrip("\n") for x in sum_of_fuel]
    sum_of_fuel = [int(x) for x in sum_of_fuel]
## For each item on a list I do a simple calculation
print(f"List without calculation :\n{sum_of_fuel}\n")
sum_of_fuel = [simple_calcul(x) for x in sum_of_fuel]
print(f"List with calculation :\n{sum_of_fuel}\n")

## Need to add each lines on the list 
result_sum_of_fuel = sum_of_element(sum_of_fuel)
print(f"The total of each element of fuel is:\n{result_sum_of_fuel}\n")

## final calculation
intermediate_fuel_calcul = sum_of_fuel.copy()
print(f"The copy is :\n{intermediate_fuel_calcul}\n")
# for i in range (len(intermediate_fuel_calcul)):
    # intermediate_fuel_calcul[i] = zero_tracking(intermediate_fuel_calcul[i])
intermediate_fuel_calcul=[zero_tracking(x) for x in intermediate_fuel_calcul]
print(f"Calculation on the copy :\n{intermediate_fuel_calcul}\n")
list_result = sum_of_fuel + intermediate_fuel_calcul
print(f"When we add 2 list, the result is :\n{list_result}\n")
final_result = sum_of_element(list_result)
print(f"The final result is :\n{final_result}\n")