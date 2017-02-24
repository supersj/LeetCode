import bisect
class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        tmp = []
        nums.reverse()
        for num in nums:
            _index = bisect.bisect_left(tmp,num)
            tmp.insert(_index,num)
            result.append(_index)
        return result.reverse()

num = [5, 2, 6, 1]
hh=Solution()
hh.countSmaller(num)