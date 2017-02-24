from heapq import *
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        q = []
        for e in points:
            e.reverse()
            heappush(q,e)
        cnt = 0
        while q:
            cnt += 1
            t = heappop(q)
            while q and q[0][1] <=  t[0]:
                heappop(q)

        return cnt

hh = Solution()
points = []
print(hh.findMinArrowShots(points))