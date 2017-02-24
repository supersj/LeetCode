# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
#
# Example 1:
#
# Input: k = 3, n = 7
#
# Output:
#
# [[1,2,4]]
#
# Example 2:
#
# Input: k = 3, n = 9
#
# Output:
#
# [[1,2,6], [1,3,5], [2,3,4]]
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        def combinationhelp(start,k,n,tmp,result):
            if len(tmp) == k and n == 0:
                result.append(tmp[:])
                return
            for i in range(start,10):
                if n-i < 0:
                    break
                tmp.append(i)
                combinationhelp(i+1, k, n-i, tmp, result)
                tmp.pop()
        result = []
        tmp = []
        combinationhelp(1,k,n,tmp,result)
        return result



