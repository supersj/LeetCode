# Follow up for "Find Minimum in Rotated Sorted Array":
# What if duplicates are allowed?
#
# Would this affect the run-time complexity? How and why?
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
#
# Find the minimum element.
#
# The array may contain duplicates.

class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1

        while left < right:
            while left < right:
                if nums[left] == nums[left + 1]:
                    left += 1
                    continue
                if nums[right] == nums[right - 1]:
                    right -= 1
                    continue
                break
            if left >= right:
                return nums[left]
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid+1
        return nums[left]
