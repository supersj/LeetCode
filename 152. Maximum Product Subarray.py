# Find the contiguous subarray within an array (containing at least one number) which has the largest product.
#
# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        r = nums[0]
        imax = r
        imin = r
        for i in range(1,len(nums)):
            if nums[i] < 0:
                imax,imin = imin,imax
            imax = max(nums[i],imax*nums[i])
            imin = min(nums[i],imin*nums[i])
            r = max(r,imax)
        return r