# Given a string S and a string T, count the number of distinct subsequences of T in S.
#
# A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).
#
# Here is an example:
# S = "rabbbit", T = "rabbit"
#
# Return 3.
# DP
class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        lens = len(s)
        lent = len(t)
        if lens < lent:
            return 0
        DP = [[0 for i in range(lent+1)] for j in range(lens+1)]
        for i in range(lent+1):
            DP[0][i] = 0
        for j in range(lens+1):
            DP[j][0] = 1
        for i in range(1,lens+1):
            for j in range(1,lent+1):
                if s[i-1] == t[j-1]:
                    DP[i][j] = DP[i-1][j-1]+DP[i-1][j]
                else:
                    DP[i][j] = DP[i-1][j]
        return DP[lens][lent]