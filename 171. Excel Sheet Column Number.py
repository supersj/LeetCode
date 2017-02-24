# Related to question Excel Sheet Column Title
#
# Given a column title as appear in an Excel sheet, return its corresponding column number.
#
# For example:
#
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        tmp = 1
        for i in range(len(s)-1,-1,-1):
            result += (ord(s[i]) - ord('A') + 1) * tmp
            tmp = tmp*26
        return result