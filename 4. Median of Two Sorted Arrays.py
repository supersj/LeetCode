import sys
class Solution(object):
    # todo very hard
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        imin = -sys.maxsize
        imax = sys.maxsize
        N1 = len(nums1)
        N2 = len(nums2)
        if N1<N2:
            return self.findMedianSortedArrays(nums2,nums1)
        if N2 == 0:
            return (nums1[(N1-1)//2] + nums1[(N1)//2]) / 2.0
        lo,hi = 0, N2*2
        while lo <= hi:
            mid2 = (lo + hi) // 2
            mid1 = N1 + N2 - mid2
            L1 = imin if mid1 == 0 else nums1[(mid1-1)//2]
            L2 = imin if mid2 == 0 else nums2[(mid2-1)//2]
            R1 = imax if mid1 == N1*2 else nums1[(mid1)//2]
            R2 = imax if mid2 == N2*2 else nums2[(mid2)//2]
            if L1 > R2:
                lo = mid2 + 1
            elif L2 > R1:
                hi = mid2 - 1
            else:
                return (max(L1,L2) + min(R1,R2))/2.0
        return -1

