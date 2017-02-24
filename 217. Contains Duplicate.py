class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashmap = {}
        for num in nums:
            if hashmap.has_key(num):
                return False
            hashmap[num] = 1
        return True