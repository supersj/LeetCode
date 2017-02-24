# Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
#
# For example, given the following triangle
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
# The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
#
# Note:
# Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        rows = len(triangle)
        if rows == 0:
            return 0
        for i in range(1,rows):
            triangle[i][0] += triangle[i-1][0]
            for j in range(1,i):
                triangle[i][j] += min(triangle[i-1][j-1],triangle[i-1][j])
            triangle[i][i] += triangle[i-1][i-1]
        return min(triangle[rows-1])