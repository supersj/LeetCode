import math
# todo  base mathmatics HEX
class Solution(object):
    def poorPigs(self, buckets, minutesToDie, minutesToTest):
        """
        :type buckets: int
        :type minutesToDie: int
        :type minutesToTest: int
        :rtype: int
        """
        n = minutesToTest//minutesToDie
        ans = math.ceil(math.log(buckets,n+1))
        return ans
hh = Solution()
print(hh.poorPigs(1000,15,60))