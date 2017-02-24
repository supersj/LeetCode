# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
#
# You may assume that the array is non-empty and the majority element always exist in the array.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        major = nums[0]
        count = 1
        for i in range(1,len(nums)):
            if count == 0:
                count += 1
            elif major == nums[i]:
                count += 1
            else:
                count -= 1
        return major
