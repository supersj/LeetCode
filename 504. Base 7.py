class Solution(object):
    def convertTo7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        result = ""
        ispositive = 1
        if num < 0:
            ispositive = -1
        num = abs(num)
        while num != 0:
            m = num % 7
            num = num // 7
            result = str(m) + result
        if ispositive == -1:
            result = '-' + result
        return result