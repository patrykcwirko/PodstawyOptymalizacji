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
    lag = []
    for l in range(len(problem.fc)):
        k = k+1
        for j in range(len(problem.fc[l])):
            if j == x and i < len(problem.fc)-1:
                if i < 2:
                    problem.fc[l][j] = problem.fc[l][j] * (i+1)
                    lag.append(problem.fc[l][j])
                i = i+1
            else:
                if i < 3 and k < 3:
                    problem.fc[l][j] = 0
        if len(problem.fc[l]) > 2:
            if problem.fc[l][(x+1)%len(problem.fc[l])] == 0:
                problem.fc[l][:] = copy.deepcopy([0] * len(problem.fc[l]))
                lag.append(0)
            else:
                a = problem.fc[l][0]
                problem.fc[l][:] = copy.deepcopy([0] * len(problem.fc[l]))
                problem.fc[l][0] = copy.deepcopy(a)
                problem.fc[l][x+1] = 1
                lag.insert(problem.fc[l].index(0), problem.fc[l][0])

    for list in problem.ogr:
        for i in range(len(list)):
            if i != x:
                list[i] = 0
            else:
                lag.append(list[i])

    # print("tstfc")
    # print(problem.fc)
    # print(problem.ogr)
    return lag



problem = load_file()
problem.lenfc = len(problem.fc[0])
problem.lenogr = len(problem.ogr) - problem.lenfc
for j in range(len(problem.fc[0])):
    problem.lag.append( copy.deepcopy(lagran(copy.deepcopy(problem), j)) )
#przekształcanie ograniczeń do zadania zastępczego
for i in range(len(problem.fc[0])):
    problem.ogr.pop( len(problem.fc[0]))
for i in range(len(problem.ogr)):
    for j in range(len(problem.ogr)):
        if i == j:
            problem.ogr[j].append(1)
        else:
            problem.ogr[j].append(0)

for i in range(len(problem.ogr) + len(problem.fc[0])*2):
    for j in range(len(problem.ogr)):
        problem.ogr[j].append(0)
for j in problem.ogr:
    problem.b.append(j.pop(2))

#przekształcanie lagrange'anów do postaci dla zadania zastępczego
for j in range(len(problem.fc[0])):
    problem.b.append(problem.lag[j].pop(0))

for j in range(len(problem.ogr)):
    for i in range(len(problem.fc[0])):
        problem.lag[i].insert(2, 0)

for i in range(len(problem.fc)-1):
    for j in range(len(problem.fc[0])):
        if i == j:
            problem.lag[j].append(1)
        else:
            problem.lag[j].append(0)

#tworzenie tablicy ze zmiennymi
problem.zm =  copy.deepcopy(problem.ogr) + copy.deepcopy(problem.lag)

#tworzenie tablicy zmiennych funkcji celu dla zadania zastępczego
problem.cx = [0]* ( len(problem.lag[0]) - len(problem.fc[0]) )
for i in range(len(problem.fc[0])):
    problem.cx.append(1)

#tworzenie wektora zmiennych bazowych
for i in range( len( problem.ogr ) ):
    problem.cb.append( [ problem.cx[i+problem.lenfc] ] )
for i in range( problem.lenfc ):
    problem.cb.append( [ problem.cx[len(problem.cx) -i -1] ] )

#tworzenie tablicy zmiennych bazowych
for j in problem.zm:
    tmp = []
    for i in range( problem.lenfc ):
        tmp.append( j[problem.lenfc+i] )
    problem.zb.append( tmp )

for j in range( len(problem.zm) ):
    problem.zb[len(problem.zm) - j -1].append( problem.zm[j][len(problem.zm) -1] )
    problem.zb[len(problem.zm) - j -1].append( problem.zm[j][len(problem.zm) -2] )

#tworzenie tablicy zmiennych nie bazowych
for j in problem.zm:
    tmp = []
    for i in range( problem.lenfc ):
        tmp.append( j[i] )
    problem.znb.append( tmp )
    # problem.znb.append( [j[0], j[1]])

for j in range( len(problem.zm) ):
    for i in range( len( problem.zm[0]) - len(problem.zb[0]) - problem.lenfc ):
        problem.znb[j].append( problem.zm[j][ i + 4] )

#Tworzenie tablicy pomocniczej z nazwami zmiennych
for i in range(problem.lenfc):
    problem.strzm.append( "x" + str(i) )
for i in range(problem.lenogr):
    problem.strzm.append( "xd" + str(i) )
for i in range(problem.lenogr):
    problem.strzm.append( "y" + str(i) )
for i in range(problem.lenfc):
    problem.strzm.append( "yd" + str(i) )
for i in range(problem.lenfc):
    problem.strzm.append( "w" + str(i) )

for i in range(problem.lenfc):
    problem.strzb.append( "xd" + str(i) )
for i in range(problem.lenfc):
    problem.strzb.append( "w" + str(i) )

print(problem.strzm)
print(problem.strzb)

problem.simplex()

#Poprawa tablicy pomocniczej
problem.strzb = []
problem.strzm = []
for i in range(problem.lenfc):
    problem.strzb.append( "xd" + str(i) )
for i in range(problem.lenfc):
    problem.strzb.append( "w" + str(i) )

problem.strzm = copy.deepcopy(problem.strzb)
for i in range(problem.lenfc):
    problem.strzm.append( "x" + str(i) )
for i in range(problem.lenogr):
    problem.strzm.append( "y" + str(i) )
for i in range(problem.lenfc):
    problem.strzm.append( "yd" + str(i) )

problem.simplex()

# print(problem.zm)
# print(problem.znb)
# print(problem.zb)
# print(problem.cx)
# print(problem.cb)
# print(problem.b)
# print(problem.ogr)
# print(problem.fc)
