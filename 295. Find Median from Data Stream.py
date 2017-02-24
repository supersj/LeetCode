# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2
from heapq import *
class MedianFinder(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.mq = []
        self.mc = 0
        self.sq = []
        self.sc = 0

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if self.mc == 0:
            heappush(self.mq, -num)
            self.mc += 1
            return
        if self.sc == 0:
            self.sc += 1
            if num < -self.mq[0]:
                tmp = heappop(self.mq)
                heappush(self.sq,-tmp)
                heappush(self.mq, -num)
            else:
                heappush(self.sq, num)
            return
        if self.mc == self.sc:
            self.mc += 1
            if num > self.sq[0]:
                tmp = heappop(self.sq)
                heappush(self.mq,-tmp)
                heappush(self.sq,num)
            else:
                heappush(self.mq,-num)
        else:
            self.sc += 1
            if num < -self.mq[0]:
                tmp = heappop(self.mq)
                heappush(self.sq,-tmp)
                heappush(self.mq, -num)
            else:
                heappush(self.sq,num)
    def findMedian(self):
        """
        :rtype: float
        """
        if self.sc == 0 and self.mc == 0:
            return 0
        if self.mc > self.sc:
            return -self.mq[0]
        return float(-self.mq[0] + self.sq[0]) / 2



        # Your MedianFinder object will be instantiated and called as such:
        # obj = MedianFinder()
        # obj.addNum(num)
        # param_2 = obj.findMedian()