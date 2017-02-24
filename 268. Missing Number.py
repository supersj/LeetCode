# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.
#
# For example,
# Given nums = [0, 1, 3] return 2.
#
# Note:
# Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
#
# Credits:
# Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        maxn = 0
        minn = len(nums)
        for i in range(len(nums)):
            sum+=nums[i]
            maxn = max(maxn,nums[i])
            minn = min(minn,nums[i])
        if minn != 0:
            return 0
        result = (maxn)*(maxn+1)//2 - sum
        if result == 0:
            return maxn+1
        return result

class Solution1(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        lens = len(nums)
        SUM = (lens+1)*lens//2
        for i in range(len(nums)):
            sum+=nums[i]
        return SUM-sum
"""
public int missingNumber(int[] nums) { //xor
    int res = nums.length;
    for(int i=0; i<nums.length; i++){
        res ^= i;
        res ^= nums[i];
    }
    return res;
}
"""