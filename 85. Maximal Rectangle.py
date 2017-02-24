# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# For example, given the following matrix:
#
# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
# Return 6.
# Subscribe to see which companies asked this question
def largestRectangleArea(heights):
    """
    :type heights: List[int]
    :rtype: int
    """
    stack = []
    maxArea = 0
    heights.append(0)
    zeroindex = 0
    for i in range(len(heights)):
        if not stack or heights[stack[-1]] <= heights[i]:
            stack.append(i)
        else:
            while stack and heights[stack[-1]] > heights[i]:
                left = stack.pop()
                if not stack:
                    maxArea = max((i-zeroindex) * heights[left], maxArea)
                else:
                    maxArea = max((i - stack[-1] - 1)*heights[left],maxArea)
            stack.append(i)
    return maxArea
def Transform(strmatrix):
    matrix = []
    for ele in strmatrix:
        matrix.append([int(e) for e in ele])
    m = len(matrix)
    n = 0
    if m >= 1:
        n = len(matrix[0])
    for i in range(1,m):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            else:
                matrix[i][j] += matrix[i-1][j]
    maxArea = 0
    for ele in matrix:
        maxArea = max(maxArea,largestRectangleArea(ele))
    print(maxArea)

class Solution(object):
    def maximalRectangle(self,matrix):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        if not matrix or not matrix[0]:
            return 0
        n = len(matrix[0])
        heights = [0] * (n + 1)
        maxArea = 0
        ans = 0
        for row in matrix:
            for i in range(n):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            stack = []
            for i in range(n+1):
                if not stack or heights[stack[-1]] <= heights[i]:
                    stack.append(i)
                else:
                    while stack and heights[stack[-1]] > heights[i]:
                        left = stack.pop()
                        if not stack:
                            maxArea = max(i * heights[left], maxArea)
                        else:
                            maxArea = max((i - stack[-1] - 1)*heights[left],maxArea)
                    stack.append(i)
            ans = max(ans,maxArea)
        return ans
    # def maximalRectangle(self,strmatrix):
    #     matrix = []
    #     for ele in strmatrix:
    #         matrix.append([int(e) for e in ele])
    #     m = len(matrix)
    #     n = 0
    #     if m >= 1:
    #         n = len(matrix[0])
    #     for i in range(1,m):
    #         for j in range(n):
    #             if matrix[i][j] == 0:
    #                 continue
    #             else:
    #                 matrix[i][j] += matrix[i-1][j]
    #     maxArea = 0
    #     for ele in matrix:
    #         maxArea = max(maxArea,self.largestRectangleArea(ele))
    #     return maxArea
matrix = ["10100","10111","11111","10010"]
Transform(matrix)