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
        stack = []
        zero= []
        for i in range(n):
            if machine[i] > ave:
                stack.append(i)
            if machine[i] == 0:
                zero.append(i)
        cnt = 0
        while stack:
            cnt += 1
            tmpstack = []
            tmpzero = []
            start = 0
            while stack and start < n:
                tmp = stack.pop(0)
                hassmaller = 0
                for i in range(start,n):
                    if machine[i] < ave:
                        hassmaller = 1
                        start = tmp + 1
                        if i < tmp:
                            p = 0
                            while zero and zero[p] < i:
                                tmpzero.append(zero.pop())
                            if zero[0] <= tmp:
                                machine[zero[i]] += 1
                                machine[tmp] -= 1
                                if machine[tmp] > ave:
                                    tmpstack.append(tmp)
                                break

                        else:
                            while stack and stack[0] < i:
                                tmpstack.append(tmp)
                                tmp = stack.pop(0)
                            start = tmp + 1
                            if machine[i] == ave - 1:
                                machine[i] += 1
                                machine[tmp] -= 1
                                if machine[tmp] > ave:
                                    tmpstack.append(tmp)
                                break
                            else:
                                if stack:
                                    if stack[0] > i:
                                        if len(stack) > 1 and stack[1] == stack[0] + 1:
                                            machine[i] += 2
                                            machine[tmp] -= 1
                                            tmp2 = stack.pop(0)
                                            machine[tmp2] -= 1
                                            if machine[tmp] > ave:
                                                tmpstack.append(tmp)
                                            if machine[tmp2] > ave:
                                                tmpstack.append(tmp2)
                                            start = tmp2 + 1
                                            break
                                        else:
                                            machine[i] += 1
                                            machine[tmp] -= 1
                                            if machine[tmp] > ave:
                                                tmpstack.append(tmp)
                                            start = i + 1
                                            break
                                    else:
                                        machine[i] += 1
                                        machine[tmp] -= 1
                                        if machine[tmp] > ave:
                                            tmpstack.append(tmp)
                                        break
                                else:
                                    machine[i] += 1
                                    machine[tmp] -= 1
                                    if machine[tmp] > ave:
                                        tmpstack.append(tmp)
                                    break
                if not hassmaller:
                    tmpstack.append(tmp)
            stack = tmpstack[:]
        return cnt
hh = Solution()
machine = [100000,0,100000,0,100000,0,100000,0,100000,0,100000,0]
print(hh.findMinMoves(machine))



