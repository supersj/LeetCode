class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        def isvalid(l1, l2, num):
            l1, l2 = l2, l1 + l2
            start = 0
            end = len(num)
            while start < end:
                lenl2 = len(str(l2))
                if num[start] == '0' and lenl2 > 1:
                    return False
                if l2 == int(num[start:min(start + lenl2, end)]):
                    start += lenl2
                    l1, l2 = l2, l1 + l2
                else:
                    return False
            return True
        ln = len(num)
        if ln < 3:
            return False
        half = ln // 2
        for endl1 in range(1,ln):
            if endl1 > half:
                return False
            l1 = int(num[0:endl1])
            if num[endl1] == '0':
                if isvalid(l1,0,num[endl1+1:]):
                    return True
                continue
            for endl2 in range(endl1 + 1,ln):
                if endl2 - endl1 > ln - endl2:
                    break
                l2 = int(num[endl1:endl2])
                if isvalid(l1,l2,num[endl2:]):
                    return True
            if l1 == 0:
                break
        return False





def isvalid(l1, l2, num):
    l1, l2 = l2, l1 + l2
    start = 0
    end = len(num)
    while start < end:
        lenl2 = len(str(l2))
        if num[start] == '0' and lenl2 > 1:
            return False
        if l2 == int(num[start:min(start + lenl2, end)]):
            start += lenl2
            l1, l2 = l2, l1 + l2
        else:
            return False
    return True
l1,l2 = 1,1
if isvalid(0,0,'000112'):
    print('Yes')
else:
    print('fuck')