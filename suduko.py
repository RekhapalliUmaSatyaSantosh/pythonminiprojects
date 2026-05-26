l=[[5,3,4,6,7,8,9,1,2],
   [6,7,2,1,9,5,3,4,8],
   [1,9,8,3,4,2,5,6,7],
   [8,5,9,7,6,1,4,2,3],
   [4,2,6,8,5,3,7,9,1],
   [7,1,3,9,2,4,8,5,6],
   [9,6,1,5,3,7,2,8,4],
   [2,8,7,4,1,9,6,3,5],
   [3,4,5,2,8,6,1,7,9]]

def row(a):
    for i in l:
        if len(set(i))!=9:
            return False
    return True

def col(b):
    r=[]

    for i in range(len(l)):
        r.append([])

        for j in range(len(l[i])):
            r[i].append(l[j][i])

    for i in r:
        if len(set(i))!=9:
            return False
    return True

def small(c):

    for i in range(0,9,3):
        for j in range(0,9,3):

            r=[]

            for n in range(i,i+3):
                for m in range(j,j+3):
                    r.append(l[n][m])

            if len(set(r))!=9:
                return False
    return True
if row(l) and col(l) and small(l):
    print('Valid')
else:
    print('Invalid')