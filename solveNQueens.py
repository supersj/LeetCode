
def setable(i,j,p,tl,tr):
    return p[j] != 1 and tl[i+j] != 1 and tr[j-i+len(p)-1]!= 1

x = 0
def solveNQueens(n,depth,p,tl,tr,result):
    """
    :type n: int
    :rtype: List[List[str]]
    """

    if depth == n:
        global x
        x += 1
        print(x, end='')
        for i in range(depth):
            print(i,": ", result[i],end='------')
        print()
    for j in range(n):
        if setable(depth,j,p,tl,tr):
            p[j] = 1
            tl[depth+j] = 1
            tr[j-depth+len(p)-1] = 1
            result[depth] = j
            solveNQueens(n,depth+1,p,tl,tr,result)
            p[j] = 0
            tl[depth+j] = 0
            tr[j-depth+len(p)-1] = 0

p = [0]*8
tl = [0]*15
tr = [0]*15
result = [0]*8

hh = solveNQueens(8,0,p,tl,tr,result)

