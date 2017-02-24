class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        result = [0,1]
        for circle in range(2,n+1):
            tmp = []
            lenth = len(result)
            for num in result[::-1]:
                tmp.append(lenth + num)
            result += tmp
        return result

hh = Solution()

print(hh.grayCode(3))