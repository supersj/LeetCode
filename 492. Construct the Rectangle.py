import math


class Solution(object):
    # todo  wrong solution it's better to from W than L
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        if not area:
            return []
        minL = math.ceil(math.sqrt(area))
        result = []
        while area % minL != 0 and minL <= area:
            minL += 1
        minW = area // minL
        return [int(minL), int(minW)]
hh = Solution()
print(hh.constructRectangle(9999991))
