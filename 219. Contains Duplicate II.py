class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        for i in range(len(nums)):
            if hashmap.has_key(nums[i]):
                if i - hashmap[nums[i]] <= k:
                    return True
            hashmap[nums[i]] = i
        return False