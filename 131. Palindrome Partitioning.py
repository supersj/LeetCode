# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s.
#
# For example, given s = "aab",
# Return
#
# [
#   ["aa","b"],
#   ["a","a","b"]
# ]
# Subscribe to see which companies asked this question





class Solution(object):

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        def DP(s):
            slen = len(s)
            table = [[False for i in xrange(slen)] for j in xrange(slen)]
            for i in xrange(slen):
                table[i][i] = True
            for i in xrange(1, slen):
                if s[i] == s[i - 1]:
                    table[i - 1][i] = True
            for k in xrange(2, slen):
                for i in xrange(slen - k):
                    if s[i] == s[i + k] and table[i + 1][i + k - 1]:
                        table[i][i + k] = True
            return table

        def dfs(result, table, tmp, row, col, s):
            if col == len(table):
                result.append(tmp[:])
            for i in xrange(col, len(table)):
                if table[row][i] == True:
                    tmp.append(s[row:i + 1])
                    dfs(result,table, tmp, i + 1, i + 1, s)
                    tmp.pop()
        result = []
        table = DP(s)
        tmp = []
        dfs(result,table, tmp, 0, 0, s)
        return result



hh = Solution()
s = "efe"
hh.partition(s)
print(hh.result)
