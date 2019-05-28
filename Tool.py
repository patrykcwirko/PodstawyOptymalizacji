from Problem import *
import copy

def load_file(file_path_FC='./Date_FC.txt', file_path_O='./Date_O.txt'):
    date1 = []
    date2 = []
    fc = []
    ogr = []
    problem = Problem()

    with open(file_path_FC, 'r') as f:
        for line in f:
            date1.append(line)

    for line in date1:
        if 'str' in line:
            break
        values = [int(i) for i in line.split()]
        fc.append(values)

    with open(file_path_O) as o:
        for line in o:
            date2.append(line)

    for line in date2:
        if 'str' in line:
            break
        values = [int(i) for i in line.split()]
        ogr.append(values)
    problem.fc = fc
    problem.ogr = ogr
    return problem

def lagran(problem, x):
    i = 0
    k = 0
    for list in problem.fc:
        k = k+1
        for j in range(len(list)):
            if j == x and i < 3:
                if i < 2:
                    list[j] = list[j] * (i+1)
                i = i+1
            else:
                if i < 3 and k < 3:
                    list[j] = 0
        if len(list) > 3:
            if list[(x+1)%len(list)] == 0:
                list[:] = copy.deepcopy([0] * len(list))
            else:
                a = list[0]
                list[:] = copy.deepcopy([0] * len(list))
                list[0] = copy.deepcopy(a)
                list[x+1] = 1
    print(problem.fc)





problem = load_file()
lagran(problem, 0)
# print(problem.ogr)
# print(problem.fc)
