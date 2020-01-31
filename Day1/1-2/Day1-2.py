##  VARIABLES
sum_of_fuel = []
final_result = 0

##  FUNCTIONS
def simple_calcul(number):
    result = (number//3)-2
    return result

def sum_of_element(list):
	sum_result = 0
	# sum_result += [list for i in range (0, len(list))]
	for i in range (len(list)-1):
		sum_result += list[i]
	return sum_result

# def scroll_list(parameter, list):
	# for parameter in range (len(list)-1):
	# return list[parameter]

def zero_tracking(list_element):
	list_element = calcul(list_element)
		while list_element > 0 :
			list_element = calcul(list_element)
			result += list_element
			return result

## I open the file which containt some integers in strings
## I put them on a list, I transform them to be ready for calculation
with open("Day1.txt") as sum_of_fuel:
    sum_of_fuel = sum_of_fuel.readlines()
    sum_of_fuel = [x.rstrip("\n") for x in sum_of_fuel]
    sum_of_fuel = [int(x) for x in sum_of_fuel]
## For each item on a list I do a simple calculation
sum_of_fuel = [simple_calcul(x) for x in sum_of_fuel]
print(f"After calculation each elements of fuel are:\n{sum_of_fuel}\n")

## Need to add each lines on the list 
result_sum_of_fuel = sum_of_element(sum_of_fuel)
print(f"The total of each element of fuel is:\n{result_sum_of_fuel}\n")

##
intermediate_fuel_calcul = sum_of_fuel.copy()
print(f"The copy is :\n{intermediate_fuel_calcul}\n")


# print(f"The final result is {calculation_loop(sum_of_fuel)}")
## I do a copy because I need to use some mathematical elements
# fuel_mass_list = sum_of_fuel.copy()
# print(f"Je suis une copie {fuel_mass_list}")
