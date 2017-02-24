# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#
# For example,
# Given [100, 4, 200, 1, 3, 2],
# The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.
#
# Your algorithm should run in O(n) complexity.
#
# Subscribe to see which companies asked this question
# TODO  no has_key in python3 ... So you need to think a way to solve the problem
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        hashdict = {}
        for num in nums:
            if not hashdict.has_key(num):
                left = hashdict[num-1] if hashdict.has_key(num-1) else 0
                right = hashdict[num+1] if hashdict.has_key(num+1) else 0
                Sum = left + right + 1
                hashdict[num] = Sum

                result = max(result, Sum)

                hashdict[num - left] = Sum
                hashdict[num + right] = Sum
            else:
                continue
        return result

nums = [100,4,200,1,3,2]

hh = Solution()
hh.longestConsecutive(nums)
