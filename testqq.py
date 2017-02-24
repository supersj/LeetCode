from heapq import *
L = []
for i in range(5):
    heappush(L,(2*i,10-i))
# for i in range(5):
#     print(heappop(L))
for i in range(5):
    print(L[0])
    heappop(L)