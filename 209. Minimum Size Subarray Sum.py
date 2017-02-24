class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        stack = []
        sum = 0
        minlen = len(nums)
        for num in nums:
            if sum < s:
                stack.append(num)
                sum += num
            if sum >= s:
                while sum >= s:
                    sum -= stack.pop(0)
                minlen = min(minlen,len(stack)+1)
        return minlen if len(nums) > len(stack) else 0
