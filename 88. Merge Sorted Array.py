class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        index = m + n - 1
        n -= 1
        m -= 1
        while n >= 0 and m >= 0:
            if nums2[n] >= nums1[m]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1
            index -= 1
        if n == -1:
            return
        else:
            for i in range(n + 1):
                nums1[i] = nums2[i]
