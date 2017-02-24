# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return the minimum cuts needed for a palindrome partitioning of s.
#
# For example, given s = "aab",
# Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.
#
# Subscribe to see which companies asked this question
class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def DP(s,slen):
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
        def findIndex(col,table):
            index = []
            for i in xrange(col+1):
                if table[i][col]:
                    index.append(i)
            return index

        slen = len(s)
        table = DP(s,slen)
        mincut = [0 for i in xrange(slen)]
        for i in xrange(1,slen):
            index = findIndex(i,table)
            if index[0] == 0:
                mincut[i] = 0
            else:
                mincut[i] = min([mincut[_index - 1]+1 for _index in index])
        return mincut[slen-1]

"""
class Solution {
public:
    int minCut(string s) {
        int n = s.size();
        vector<int> cut(n+1, 0);  // number of cuts for the first k characters
        for (int i = 0; i <= n; i++) cut[i] = i-1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; i-j >= 0 && i+j < n && s[i-j]==s[i+j] ; j++) // odd length palindrome
                cut[i+j+1] = min(cut[i+j+1],1+cut[i-j]);

            for (int j = 1; i-j+1 >= 0 && i+j < n && s[i-j+1] == s[i+j]; j++) // even length palindrome
                cut[i+j+1] = min(cut[i+j+1],1+cut[i-j+1]);
        }
        return cut[n];
    }
};

"""
