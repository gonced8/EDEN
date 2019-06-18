from random import randint

def generate_shape (npoints):
    list = [[0,0]]
    free=get_free([0, 0], list)
    for i in range (0, npoints-1):
        index = randint(0, len(free)-1)
        point = free.pop(index)
        list.append(point)
        free=free+get_free(point, list)
        free = remove_duplicates(free)
    return list

def get_free (point, list):
    free=[]
    for i in range (-1, 2):
        for j in range (-1, 2):
            new_point=[point[0]+i, point[1]+j]
            #if abs(i)==abs(j):  # Ignore points in the diagonal
                #continue
            if new_point in list:
                continue
            free.append(new_point)
    return free

def remove_duplicates(list):
    new_list = []
    for elem in list:
        if elem not in new_list:
            new_list.append(elem)
    return new_list


def print_shape(list):
    lenght = len(list)
    matrix=[[' ' for i in range(2*lenght)] for j in range(2*lenght)]
    for elem in list:
        matrix[elem[0]+lenght][elem[1]+lenght] = 'O'
    for row in matrix:
        print(row)

'''
list=generate_shape(8)
print(list)
print_shape(list)
'''
