class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return nums
        result = []
        _max = max(nums[0:k])
        _index = 0
        for i in range(k):
            if nums[i] == _max:
                _index = i
        result.append(nums[_index])
        nlen = len(nums)
        for i in range(k,nlen):
            if nums[i] < nums[_index]:
                if i - _index < k:
                    result.append(nums[_index])
                else:
                    tmpmax = nums[_index + 1]
                    for j in range(_index+1,i+1):
                        if nums[j] >= tmpmax:
                            tmpmax  = nums[j]
                            _index = j
                    result.append(tmpmax)
            else:
                result.append(nums[i])
                _index = i
        return result

nums = [9,10,9,-7,-4,-8,2,-6]
k = 5
hh = Solution()
hh.maxSlidingWindow(nums,k)