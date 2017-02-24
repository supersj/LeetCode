# a = input("the first:   ")
# b = input("the second:  ")

def canjumpII(nums):
    numslen = len(nums)
    curmax = 0
    last = 0
    minimum = 0
    tmplast = 0
    if numslen == 1:
        return 0
    while curmax < numslen-1:
        minimum += 1
        for jump in range(nums[last]+1):
            if last + jump >= numslen - 1:
                return minimum
            if nums[last+jump]+last+jump > curmax:
                curmax = nums[last+jump]+last+jump
                tmplast = last+jump
        last = tmplast
    return minimum + 1

nums = [2,3,4,5,1,1,2,11,1,1,1,1,1,1,1,1,1,1,1,1,1]
print(canjumpII(nums))

def canjump(nums):
    reachable = 0
    for i in range(len(nums)):
        if i > reachable:
            return False
        reachable = max(reachable, nums[i]+i)
    return True





def LCSLength(X, Y):
    m = len(X)
    n = len(Y)
    C = [[0 for x in range(n+1)] for y in range(m+1)]
    for i in range(m+1):
        C[i][0] = 0
    for i in range(n+1):
        C[0][i] = 0
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1] == Y[j-1]:
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1],C[i-1][j])
    return C[m][n],C

def backtrack(C, X, Y, i, j):
    if  i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backtrack(C,X,Y,i-1,j-1)+X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backtrack(C,X,Y,i,j-1)
        else:
            return backtrack(C,X,Y,i-1,j)


def backtrackAll(C, X, Y, i, j):
    if i == 0 or j == 0:
        return set([""])
    elif X[i-1] == Y[j-1]:
        return set([z+X[i-1] for z in backtrackAll(C, X, Y, i-1, j-1)])
    else:
        R = set([])
        if C[i][j-1] >= C[i-1][j]:
            R.update(backtrackAll(C, X, Y, i, j-1))
        if C[i-1][j] >= C[i][j-1]:
            R.update(backtrackAll(C, X, Y, i-1, j))
        return R

# hh,C = LCSLength(a,b)
# ss = backtrackAll(C,a,b,len(a),len(b))
# print(C)
# print(ss)
# print(hh)