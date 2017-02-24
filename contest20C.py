class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        maxsize = -1
        startindex = 0
        sumleft = [0]*n
        _min = nums[0]
        _max = nums[0]

        for i in range(0,n):
            if nums[i] == 0:
                sumleft[i] = sumleft[i-1] - 1
            else:
                sumleft[i] = sumleft[i-1] + 1
            if sumleft[i] < _min:
                _min = sumleft[i]
            if sumleft[i] > _max:
                _max = sumleft[i]
        hasmap = [0]*(_max-_min + 1)
        for i in range(_max-_min+1):
            hasmap[i] = -1
        for i in range(n):
            if sumleft[i] == 0:
                maxsize = i + 1
                startindex = 0
            if hasmap[sumleft[i] - _min] == -1:
                hasmap[sumleft[i]- _min] = i
            else:
                if (i - hasmap[sumleft[i] - _min]) > maxsize:
                    maxsize = i - hasmap[sumleft[i] - _min]
                    startindex = hasmap[sumleft[i] - _min] + 1
        if maxsize == -1:
            return 0
        return maxsize
nums = [1,0,1,1,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1,1]
hh = Solution()
print(hh.findMaxLength(nums))