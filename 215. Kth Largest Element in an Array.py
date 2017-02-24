# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# For example,
# Given [3,2,1,5,6,4] and k = 2, return 5.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        start = 0
        end = len(nums)
        while start < end:
            tmp = nums[start]
            index = start + 1
            for i in range(start + 1,len(nums)):
                if nums[i] <= tmp:
                    continue
                else:
                    if i > index:
                        nums[index],nums[i] = nums[i],nums[index]
                    index += 1
            nums[start],nums[index-1] = nums[index-1],nums[start]
            if index == k:
                return nums[index-1]
            if index < k:
                start = index




hh = Solution()
nums =  [1,1]
print(hh.findKthLargest(nums,1))