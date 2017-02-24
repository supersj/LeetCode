class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def robhelp(nums):
            """
            :type nums: List[int]
            :rtype: int
            """
            if not nums:
                return 0
            nlen = len(nums)
            if nlen == 1:
                return nums[0]
            if nlen == 2:
                return max(nums)
            result = [0 for i in range(nlen)]
            result[0] = nums[0]
            result[1] = max(nums[0],nums[1])
            for i in range(2,nlen):
                result[i] = max(result[i-1],result[i-2]+nums[i])
            return result[nlen-1]
        nlen = len(nums)
        if nlen < 2:
            return max(nums)
        one = robhelp(nums[:-1])
        two = robhelp(nums[1:])
        return max(one,two)
