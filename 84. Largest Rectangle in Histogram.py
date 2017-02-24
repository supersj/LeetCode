# For example,
# Given heights = [2,1,5,6,2,3],
# return 10.
class Solution(object):
    def largestRectangleArea(self, heights):
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
hh = Solution()
print(hh.largestRectangleArea([3,6,5,7,4,8,1,0]))