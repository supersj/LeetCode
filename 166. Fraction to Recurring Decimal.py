# Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in parentheses.
#
# For example,
#
# Given numerator = 1, denominator = 2, return "0.5".
# Given numerator = 2, denominator = 1, return "2".
# Given numerator = 2, denominator = 3, return "0.(6)".
# Hint:
#
# No scary math, just apply elementary math knowledge. Still remember how to perform a long division?
# Try a long division on 4/9, the repeating part is obvious. Now try 4/333. Do you see a pattern?
# Be wary of edge cases! List out as many test cases as you can think of and test your code thoroughly.

class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        positive = 1
        if numerator * denominator < 0:
            positive = -1
        numerator = abs(numerator)
        denominator = abs(denominator)
        hashmap = {}
        stack = []
        beforeDecimal = numerator // denominator
        left = numerator % denominator
        index = 0
        if left == 0:
            if positive == -1:
                return '-' + str(beforeDecimal)
            return str(beforeDecimal)
        while left not in hashmap.keys():
            hashmap[left] = index
            index += 1
            tmp = left*10//denominator
            left = left*10%denominator
            stack.append(str(tmp))
            if left == 0:
                break
        if left != 0:
            stack.insert(hashmap[left],'(')
            stack.append(')')
        if positive == -1:
            return '-'+str(beforeDecimal) + '.' + ''.join(stack)
        return str(beforeDecimal)+'.'+''.join(stack)

hh = Solution()
hh.fractionToDecimal(-2147483648,1)