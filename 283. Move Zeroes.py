# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
#
# For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].
#
# Note:
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        nlen = len(nums)
        if nlen <= 1:
            return
        start = 0
        for i in range(nlen):
            if nums[i] == 0:
                start = i
                break
        if start == nlen - 1:
            return
        right = start + 1
        while right < nlen:
            if nums[right] == 0:
                right += 1
                continue
            else:
                nums[right],nums[start] = nums[start],nums[right]
                start += 1
                right += 1
nums = [0]
hh =Solution()
hh.moveZeroes(nums)