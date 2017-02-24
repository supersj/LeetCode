# Given a list of non negative integers, arrange them such that they form the largest number.
#
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
#
# Note: The result may be very large, so you need to return a string instead of an integer.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question
import  functools
class Solution:
    # @param {integer[]} nums
    # @return {string}

    def _cmp(self,x, y):
        a = int(str(x) + str(y))
        b = int(str(y) + str(x))
        if a > b:
            return 1
        elif b < a:
            return -1
        else:
            return 0

    def largestNumber(self, nums):
        result = [str(ele) for ele in nums]
        def _cmp( x, y):
            a = x + y
            b = y + x
            if a > b:
                return -1
            elif b < a:
                return 1
            else:
                return 0
        result.sort(key = functools.cmp_to_key(_cmp))
        index = len(result)-1
        for i in range(len(result)):
            if result[i]!= '0':
                index = i
                break
        result[:index] = []
        return ''.join(result)

hh = Solution()
nums = [0,0]
print(hh.largestNumber(nums))