class Solution(object):
    # partition is a nlogn way
    # todo this is done by bucket sort
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        n = len(citations)
        buckets = [0 for i in range(0,n+1)]
        for c in citations:
            if c>= n:
                buckets[n] += 1
            else:
                buckets[c] += 1
        cnt = 0
        for i in range(n,-1,-1):
            cnt += buckets[i]
            if cnt >= i:
                return i
        return 0


