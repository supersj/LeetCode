# TODO please attention to the detail

class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        a = version1.split('.')
        b = version2.split('.')
        lena = len(a)
        lenb = len(b)
        l = min(lena,lenb)
        for i in range(l):
            if int(a[i]) == int(b[i]):
                continue
            if int(a[i]) > int(b[i]):
                return 1
            else:
                return -1
        if lena == lenb:
            return 0
        elif lena > lenb:
            for i in range(lenb,lena):
                if int(a[i])>0:
                    return 1
            return 0
        else:
            for i in range(lena,lenb):
                if int(b[i])>0:
                    return -1
            return 0