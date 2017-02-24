# Follow up for "Remove Duplicates":
# What if duplicates are allowed at most twice?
#
# For example,
# Given sorted array nums = [1,1,1,2,2,3],
#
# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3. It doesn't matter what you leave beyond the new length.
#
# Subscribe to see which companies asked this question
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return len(nums)
        result = 1
        k = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i - 1]:
                result += 1
                nums[result-1] = nums[i]
                k = 1
            else:
                if k == 1:
                    k += 1
                    result += 1
                    nums[result - 1] = nums[i]
                else:
                    k += 1
        return result
a = Solution()
a.removeDuplicates([1,1,1,2,2,3])