# TODO wrong solution
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        stack = []
        result = []
        for price in prices:
            if not stack or price > stack[-1]:
                stack.append(price)
            else:
                profit = stack[-1] - stack[0]
                if profit > 0:
                    result.append(profit)
                stack = [price]
        if stack:
            profit = stack[-1] - stack[0]
            result.append(profit)
        result.sort()
        return sum(result[-2:])
hh = Solution()
prices = [1,2,4,2,5,7,2,4,9,0]
hh.maxProfit(prices)

import sys
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sell1 = 0
        sell2 = 0
        buy1 = -sys.maxsize
        buy2 = -sys.maxsize
        for price in prices:
            buy1 = max(buy1,-price)
            sell1 = max(sell1,buy1+price)
            buy2 = max(buy2,sell1-price)
            sell2 = max(sell2,buy2+price)
        return sell2