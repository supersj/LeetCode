# Given a positive integer, return its corresponding column title as appear in an Excel sheet.
#
# For example:
#
#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB

class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''
        result = ''
        while n > 0:
            tmp = n%26
            # todo this is not the same with the normal sotuations
            if tmp == 0:
                result = 'Z' + result
                n = n // 26
                n -= 1
                continue
            n = n // 26
            result = chr(ord('A') + tmp -1 )+result
        return result