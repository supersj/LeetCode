# Given an integer n, return the number of trailing zeroes in n!.
#
# Note: Your solution should be in logarithmic time complexity.
#
# Credits:
# Special thanks to @ts for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

# todo  interesting
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        while n // 5:
            count += n // 5
            n = n //5
        return count
