# A message containing letters from A-Z is being encoded to numbers using the following mapping:
#
# 'A' -> 1
# 'B' -> 2
# ...
# 'Z' -> 26
# Given an encoded message containing digits, determine the total number of ways to decode it.
#
# For example,
# Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
#
# The number of ways decoding "12" is 2.
#
# Subscribe to see which companies asked this question

# recursion is not the key or not the solution of this problem
# So you need to work out a dp solution for this problem

# 用了一个dict进行了优化


# Dynamic Programming
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = {}
        def numberhelp(s, start, end,dict):
            left = 0
            right = 0
            if start == end:
                return 1
            if int(s[start]) == 0:
                return 0
            if start + 1 == end:
                return 1
            if int(s[start]) != 0:
                if start+1 in dict.keys():
                    left = dict[start+1]
                else:
                    left = numberhelp(s, start+1, end,dict)
                    dict[start+1] = left
            if 10<=(int(s[start])*10+ int(s[start+1])) <=26:
                if start+2 in dict.keys():
                    right = dict[start+2]
                else:
                    right = numberhelp(s, start+2, end,dict)
                    dict[start+2] = right
            return left + right
        if len(s) == 0:
            return 0
        return numberhelp(s,0,len(s),dict)

hh = Solution()
s = "1111"
print(hh.numDecodings(s))

