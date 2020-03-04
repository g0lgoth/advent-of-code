from __future__ import division
import file_management as fm

def global_move(list):
    """
    Wait for a list with str and int and give at the end a list of int
    :param initial_list:
    :return:
    """
    x, y = 0, 0
    vector = [x, y]
    vector_list = []
    for element in range (len(list)):
        if list[element][:1] == "R":
            element_number = int(list[element][1:])
            vector = [vector[0]+element_number, vector[1]]
            vector_list.append(vector)
        elif list[element][:1] == "L":
            element_number = int(list[element][1:])
            vector = [vector[0]-element_number, vector[1]]
            vector_list.append(vector)
        elif list[element][:1] == "U":
            element_number = int(list[element][1:])
            vector = [vector[0], vector[1]+element_number]
            vector_list.append(vector)
        else:
            element_number = int(list[element][1:])
            vector = [vector[0], vector[1] - element_number]
            vector_list.append(vector)
    return vector_list

def calcul_distance(coordinate_x, coordinate_y, distance):
    if coordinate_x < 0:
        coordinate_x = -(coordinate_x)
    if coordinate_y < 0:
        coordinate_y = -(coordinate_y)
    new_distance = coordinate_x + coordinate_y
    if new_distance <= distance:
        distance = new_distance
        return distance
    else:
        return distance

def check_cross_segment(vector_list1, vector_list2):
    cross_vector_list = []
    distance = 999
    for vector1 in range((len(vector_list1))-1):
        for vector2 in range((len(vector_list2))-1):
            cross_vector = []
            if vector_list1[vector1][0] == vector_list1[vector1+1][0]:
                if vector_list2[vector2][0] <= vector_list1[vector1][0] <= vector_list2[vector2+1][0] or\
                        vector_list2[vector2][0] >= vector_list1[vector1][0] >= vector_list2[vector2+1][0]:
                    if vector_list1[vector1][1] <= vector_list2[vector2][1] <= vector_list1[vector1+1][1] or\
                            vector_list1[vector1][1] >= vector_list2[vector2][1] >= vector_list1[vector1+1][1]:
                        print("prout x", distance, vector_list1[vector1][0], vector_list2[vector2][1])
                        distance = calcul_distance(vector_list1[vector1][0], vector_list2[vector2][1], distance)
                        # cross_vector.append(vector_list1[vector1][0])
                        # cross_vector.append(vector_list2[vector2][1])
                        # cross_vector_list.append(cross_vector)
            elif vector_list1[vector1][1] == vector_list1[vector1+1][1]:
                if vector_list2[vector2][1] <= vector_list1[vector1][1] <= vector_list2[vector2+1][1] or\
                        vector_list2[vector2][1] >= vector_list1[vector1][1] >= vector_list2[vector2+1][1]:
                    if vector_list1[vector1][0] <= vector_list2[vector2][0] <= vector_list1[vector1+1][0] or\
                            vector_list1[vector1][0] >= vector_list2[vector2][0] >= vector_list1[vector1+1][0]:
                        print("prout y", distance, vector_list2[vector2][0], vector_list1[vector1][1])
                        distance = calcul_distance(vector_list2[vector2][0], vector_list1[vector1][1], distance)
                        # cross_vector.append(vector_list2[vector2][0])
                        # cross_vector.append(vector_list1[vector1][1])
                        # cross_vector_list.append(cross_vector)
    return distance

wire_list1 = fm.open_file_return_list_splitted("test1-1.txt")
wire_list2 = fm.open_file_return_list_splitted("test1-2.txt")

# wire_list1 = fm.open_file_return_list_splitted("test2-1.txt")
# wire_list2 = fm.open_file_return_list_splitted("test2-2.txt")

# wire_list1 = fm.open_file_return_list_splitted("test3-1.txt")
# wire_list2 = fm.open_file_return_list_splitted("test3-2.txt")

# wire_list1 = fm.open_file_return_list_splitted("wire_list1.txt")
# wire_list2 = fm.open_file_return_list_splitted("wire_list2.txt")

vector_list1 = global_move(wire_list1)
vector_list2 = global_move(wire_list2)
print(vector_list1)
print(vector_list2, "\n")
distance = check_cross_segment(vector_list1, vector_list2)
print(distance)


# def vector_in_line(vector1, vector2):
#     A = (vector1[1] - vector2[1])
#     B = (vector2[0] - vector1[0])
#     C = (vector1[0]*vector2[1] - vector2[0]*vector1[1])
#     return A, B, -C
#
# def intersection(line1, line2):
#     D = line1[0] * line2[1] - line1[1] * line2[0]
#     Dx = line1[2] * line2[1] - line1[1] * line2[2]
#     Dy = line1[0] * line2[2] - line1[2] * line2[0]
#     if D != 0:
#         x = Dx / D
#         y = Dy / D
#         print(x, y)
#         return x,y