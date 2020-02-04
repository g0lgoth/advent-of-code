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

# def zero_tracking(list_element, iteration):
def zero_tracking(list_element):
    list_element = simple_calcul(list_element)
    result = list_element
    # z = 1
    # print(f"test{iteration} / iteration n°{z} / calculation number {list_element} / result is {result}\n")
    while simple_calcul(list_element) > 0 :
        # z += 1
        list_element = simple_calcul(list_element)
        result += list_element
        # print(f"test{iteration} / iteration n°{z} / calculation number {list_element} / result is {result}\n")
    return result

## I open the file which containt some integers in strings
## I put them on a list, I transform them to be ready for calculation
with open("Day1.txt") as sum_of_fuel:
    sum_of_fuel = sum_of_fuel.readlines()
    sum_of_fuel = [x.rstrip("\n") for x in sum_of_fuel]
    sum_of_fuel = [int(x) for x in sum_of_fuel]
## For each item on a list I do a simple calculation
print(f"After calculation each elements of fuel are:\n{sum_of_fuel}\n")
sum_of_fuel = [simple_calcul(x) for x in sum_of_fuel]

## Need to add each lines on the list 
result_sum_of_fuel = sum_of_element(sum_of_fuel)
print(f"The total of each element of fuel is:\n{result_sum_of_fuel}\n")

## 
intermediate_fuel_calcul = sum_of_fuel.copy()
print(f"The copy is :\n{intermediate_fuel_calcul}\n")
for i in range (len(intermediate_fuel_calcul)):
# for i in range (2):
	# intermediate_fuel_calcul[i] = zero_tracking(intermediate_fuel_calcul[i], i)
    intermediate_fuel_calcul[i] = zero_tracking(intermediate_fuel_calcul[i])
print(f"The additional fuel which is needed for our rocket is in this table :\n{intermediate_fuel_calcul}\n")
final_sum_of_fuel = sum_of_element(intermediate_fuel_calcul) + result_sum_of_fuel
print(f"\n{sum_of_element(intermediate_fuel_calcul)}\n")
print(f"\n\nThe final result is :\n\n{final_sum_of_fuel}")

# print(f"The final result is {calculation_loop(sum_of_fuel)}")
## I do a copy because I need to use some mathematical elements
# fuel_mass_list = sum_of_fuel.copy()
# print(f"Je suis une copie {fuel_mass_list}")
