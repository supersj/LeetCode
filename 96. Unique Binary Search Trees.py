class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = [1 for i in range(n+1)]
        for i in range(2,n+1):
            for j in range(1,i+1):
                result[i] +=result[j-1] * result[i-j]
        return result[n]