class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        stack = []
        for price in prices:
            if not stack or price > stack[-1]:
                stack.append(price)
            else:
                profit += stack[-1] - stack[0]
                stack = [price]
        if stack:
            profit += stack[-1] - stack[0]
        return profit