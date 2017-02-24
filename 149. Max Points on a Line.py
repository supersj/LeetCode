# Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
#
# Subscribe to see which companies asked this question
# Definition for a point.
class Point(object):
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
# TODO
class Solution(object):
    def gcd(self,a,b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        if not points:
            return 0
        plen = len(points)
        if plen <= 2:
            return plen
        map = {}
        result = 0
        for i in range(plen):
            map.clear()
            overlap, _max = 0, 0
            for j in range(i+1,plen):
                x = points[j].x - points[i].x
                y = points[j].y - points[i].y
                if x == 0 and y == 0:
                    overlap += 1
                    continue
                _gcd = self.gcd(x,y)
                if _gcd != 0:
                    x /= _gcd
                    y /= _gcd
                if x in map.keys():
                    if y in map[x].keys():
                        map[x][y] += 1
                    else:
                        map[x][y] = 1
                else:
                    m = {}
                    m[y] = 1
                    map[x] = m
                _max = max(_max,map[x][y])
            result = max(result,_max + overlap + 1)
        return result
