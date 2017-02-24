# todo fuck amazing

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        tmp = 0
        for num in nums:
            tmp ^= num
        tmp &= -tmp
        result = [0,0]
        for num in nums:
            if (num & tmp) == 0:
                result[0] ^= num
            else:
                result[1] ^= num
        return result
