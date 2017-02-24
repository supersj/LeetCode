def makeNext(p):
    q = 0
    k = 0
    m = len(p)
    next = [0 for i in range(m)]
    for q in range(1,m):
        while k>0 and p[q] != p[k]:
            k = next[k-1]
        if p[q] == p[k]:
            k+=1
        next[q] = k
    print(next)

p = "ababa#ababa"
makeNext(p)