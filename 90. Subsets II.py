# Given a collection of integers that might contain duplicates, nums, return all possible subsets.
#
# Note: The solution set must not contain duplicate subsets.
#
# For example,
# If nums = [1,2,2], a solution is:
#
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
# Subscribe to see which companies asked this question

class Solution(object):
    def subsetsHelp(self,nums, start, n, result, stack):
        if n == 0:
            result.append(stack[:])
            return
        i = start
        while start <= i < len(nums) - n + 1:
            stack.append(nums[i])
            self.subsetsHelp(nums, i + 1, n - 1, result, stack)
            tmp = stack.pop()
            while i + 1 < len(nums) and tmp == nums[i + 1]:
                i += 1
            i += 1

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        stack = []
        for i in range(len(nums)+1):
            self.subsetsHelp(nums,0,i,result,stack)
        return result



def subsetsHelp(nums,start,n,result,stack):
    if n == 0:
        result.append(stack[:])
        return
    i = start
    while start <= i < len(nums) - n + 1:
        stack.append(nums[i])
        subsetsHelp(nums,i+1,n-1,result,stack)
        tmp = stack.pop()
        while i+1 < len(nums) and tmp == nums[i+1]:
            i+=1
        i += 1


result = []
stack = []
hello = []
nums = [1,2,3,3,3,4,5]
n = 2
subsetsHelp(nums,0,0,result,stack)
hello += result
print(hello)

hh = Solution()
nums = [1,2,3]
print(hh.subsetsWithDup(nums))
