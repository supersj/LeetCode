# Say you have an array for which the ith element is the price of a given stock on day i.
#
# Design an algorithm to find the maximum profit. You may complete at most k transactions.
#
# Note:
# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
#
# Credits:
# Special thanks to @Freezen for adding this problem and creating all test cases.

class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if k >= length//2:
            return self.quickSolve(prices)
        t = [[0 for i in range(length)] for j in range(k+1)]
        for i in range(1,k+1):
            tmpMax = -prices[0]
            for j in range(1,length):
                t[i][j] = max(t[i][j-1],prices[j]+tmpMax)
                tmpMax = max(tmpMax,t[i-1][j-1] - prices[j])
        return t[k][length-1]


    def quickSolve(self,prices):
        profit = 0
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                profit += prices[i] - prices[i-1]
        return profit