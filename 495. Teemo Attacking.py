class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        result = 0
        for i in range(1, len(timeSeries)):
            result += min(timeSeries[i] - timeSeries[i - 1], duration)
        result += duration
        return result
