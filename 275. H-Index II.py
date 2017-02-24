class Solution(object):
    # todo
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        length = len(citations)
        first = 0
        cnt = length
        while cnt > 0:
            step = cnt //2
            mid = first + step
            if citations[mid] < length - mid:
                first = mid + 1
                cnt -= step + 1
            else:
                cnt = step
        return length - first