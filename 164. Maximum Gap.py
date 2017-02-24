# Given an unsorted array, find the maximum difference between the successive elements in its sorted form.
#
# Try to solve it in linear time/space.
#
# Return 0 if the array contains less than 2 elements.
#
# You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
#
# Credits:
# Special thanks to @porker2008 for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question
import math
import math


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nlen = len(nums)
        if nlen < 2:
            return 0
        _max = max(nums)
        _min = min(nums)
        gap = math.ceil((_max - _min) / (nlen - 1))
        bucketMin = [2147483647] * (nlen - 1)
        bucketMax = [-2147483647] * (nlen - 1)
        for i in nums:
            if i == _min or i == _max:
                continue
            idx = math.floor((i - _min) / gap)
            bucketMin[idx] = min(bucketMin[idx], i)
            bucketMax[idx] = max(bucketMax[idx], i)
        maxgap = 0
        previous = _min
        for i in range(nlen - 1):
            if bucketMin[i] == 2147483647 and bucketMax[i] == -2147483647:
                # empty bucket
                continue
            maxgap = max(maxgap, bucketMin[i] - previous)
            previous = bucketMax[i]
        # consider max
        maxgap = max(maxgap, _max - previous)
        print(maxgap)
        return maxgap
hh = Solution()
# nums = [12115,10639,2351,29639,31300,11245,16323,24899,8043,4076,17583,15872,19443,12887,5286,6836,31052,25648,17584,24599,13787,24727,12414,5098,26096,23020,25338,28472,4345,25144,27939,10716,3830,13001,7960,8003,10797,5917,22386,12403,2335,32514,23767,1868,29882,31738,30157,7950,20176,11748,13003,13852,19656,25305,7830,3328,19092,28245,18635,5806,18915,31639,24247,32269,29079,24394,18031,9395,8569,11364,28701,32496,28203,4175,20889,28943,6495,14919,16441,4568,23111,20995,7401,30298,2636,16791,1662,27367,2563,22169,1607,15711,29277,32386,27365,31922,26142,8792]
nums = [1,3,10]
hh.maximumGap(nums)