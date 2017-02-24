# Given numRows, generate the first numRows of Pascal's triangle.
#
# For example, given numRows = 5,
# Return
#
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]
# Subscribe to see which companies asked this question

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        result = [[1]]
        for i in range(1,numRows):
            tmp = [1]
            for j in range(1,i):
                tmp.append(result[i-1][j-1]+result[i-1][j])
            tmp.append(1)
            result.append(tmp[:])
        return result