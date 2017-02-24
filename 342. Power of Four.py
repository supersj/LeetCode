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
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0:
            return False
        # strmas = "01010101"*4
        # strmas += "01010100"
        mask = 1431655765
        M = num&(~mask)
        if M==0:
            if (num&(num-1)):
                return False
            else:
                return True
        return False