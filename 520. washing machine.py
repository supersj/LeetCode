class Solution(object):
    def findMinMoves(self, machine):
        """
        :type machine: List[int]
        :rtype: int
        """
        n = len(machine)
        dresssum = 0
        for i in range(n):
            dresssum += machine[i]
        if dresssum % n != 0:
            return -1
        ave = dresssum // n
        maxIndex = []
        zeroIndex = []
        for i in range(n):
            if machine[i] > ave:
                maxIndex.append(i)
            if machine[i] == 0:
                zeroIndex.append(i)
        cnt = 0
        while maxIndex:
            cnt += 1
            tmpmax = []
            tmpzero = []
            start = 0
            while maxIndex and start < n:
                hassmaller = 0
                maxdex = maxIndex.pop(0)
                for i in range(start,n):
                    if machine[i] >= ave:
                        continue
                    hassmaller = 1
                    start = maxdex + 1
                    # right maxvalue
                    if i < maxdex:
                        placeindex = i
                        while zeroIndex and zeroIndex[0] < i:
                            tmpzero.append(zeroIndex.pop(0))
                        if zeroIndex and zeroIndex[0] > maxdex:
                            placeindex = i
                        else:
                            while zeroIndex and zeroIndex[0] < maxdex:
                                tmpzero.append(zeroIndex.pop(0))
                            if zeroIndex:
                                placeindex = zeroIndex[0]
                                zeroIndex.pop(0)
                        machine[placeindex] += 1
                        machine[maxdex] -= 1
                        if machine[maxdex] > ave:
                            tmpmax.append(maxdex)
                        break
                    else:
                        while maxIndex and maxIndex[0] < i:
                            tmpmax.append(maxdex)
                            maxdex = maxIndex.pop(0)
                        if not maxIndex:
                            if zeroIndex and i == zeroIndex[0]:
                                zeroIndex.pop(0)
                            machine[i] += 1
                            machine[maxdex] -= 1
                            if machine[maxdex] > ave:
                                tmpmax.append(maxdex)
                            start = i + 1
                            break
                        else:
                            start = i + 1
                            if zeroIndex and i == zeroIndex[0]:
                                zeroIndex.pop()
                            if machine[i] == ave - 1:
                                machine[i] += 1
                                machine[maxdex] -= 1
                                if machine[maxdex] > ave:
                                    tmpmax.append(maxdex)
                                break
                            else:
                                if len(maxIndex) > 1 and maxIndex[1] == maxIndex[0] + 1 and maxIndex[0] == i + 1 or\
                                                                len(maxIndex) == 1 and maxIndex[0] == i + 1 and i + 1 == n-1:
                                    machine[i] += 2
                                    machine[maxdex] -= 1
                                    maxdex2 = maxIndex.pop(0)
                                    machine[maxdex2] -= 1
                                    if machine[maxdex] > ave:
                                        tmpmax.append(maxdex)
                                    if machine[maxdex2] > ave:
                                        tmpmax.append(maxdex2)
                                    start = maxdex2 + 1
                                    break
                                else:
                                    machine[i] += 1
                                    machine[maxdex] -= 1
                                    if machine[maxdex] > ave:
                                        tmpmax.append(maxdex)
                                    break
                if not hassmaller:
                    tmpmax.append(maxdex)
            maxIndex = tmpmax[:]
            zeroIndex = tmpzero[:]+zeroIndex[:]
        return cnt
hh = Solution()
machine = [2,4,3,1,5]
print(hh.findMinMoves(machine))



