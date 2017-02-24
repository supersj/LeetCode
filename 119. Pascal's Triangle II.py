# Given an index k, return the kth row of the Pascal's triangle.
#
# For example, given k = 3,
# Return [1,3,3,1].
#
# Note:
# Could you optimize your algorithm to use only O(k) extra space?
#
# Subscribe to see which companies asked this question

class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        def C(m,n):
            if m == 0:
                return 1
            up = 1
            down = 1
            while n>0:
                up *= m
                m -= 1
                down*=n
                n -= 1
            return up//down
        result = []
        for i in range(rowIndex+1):
            result.append(C(rowIndex,i))
        return result