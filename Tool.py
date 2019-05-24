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





problem = load_file()
print(problem.ogr)
print(problem.fc)
