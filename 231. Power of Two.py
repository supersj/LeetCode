# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
#
# Example:
# Given num = 16, return true. Given num = 5, return false.
#
# Follow up: Could you solve it without loops/recursion?
#
# Credits:
# Special thanks to @yukuairoy for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question
class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type num: int
        :rtype: bool
        """
        # TODO n&(n-1)  is the key
        if n == 0:
            return False
        # strmas = "11111111"*3
        # strmas += "11111111"
        if (n & (n - 1)):
            return False
        else:
            return True

"""

class Solution(object):
    def isPowerOfTwo(self, n):
"""
     # TODO n&(n-1)  is the key  注意简写 就是尽量一行代码搞定有时候
"""
        # if n == 0:
        #     return False
        # strmas = "11111111"*3
        # strmas += "11111111"
        return not n&(n-1) if n != 0 else False
"""
hh = Solution()
hh.isPowerOfTwo(1)