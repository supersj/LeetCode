import math

# todo  wtf  the answe
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """

        def build(s, id, l, r, nums):
            if l == r:
                s[id] = nums[l]
                return
            mid = (l + r) // 2
            build(s, id * 2+1, l, mid, nums)
            build(s, id * 2+2, mid+1, r, nums)
            s[id] = s[id * 2+1] + s[id * 2 + 2]

        self.nums = nums
        if not nums:
            return
        h = math.ceil(math.log(len(nums), 2))
        maxsize = 2*math.pow(2, h) - 1
        self.st = [0 for i in range(int(maxsize))]
        build(self.st, 0, 0, len(nums)-1, nums)

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        def helper(st, ss, se, qs, qe, si):
            if qs <= ss and qe >= se:
                return st[si]
            if se < qs or ss > qe:
                return 0
            mid = ss + (se - ss) // 2
            return helper(st, ss, mid, qs, qe, 2 * si+1) + helper(st, mid + 1, se, qs, qe, 2 * si + 2)
        return helper(self.st, 0, len(self.nums)-1, i, j, 0)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        def updatehelp(ss, se, i, diff, si):
            if i < ss or i > se:
                return
            self.st[si] += diff
            if se != ss:
                mid = (ss + se)//2
                updatehelp(ss,mid,i,diff,2*si + 1)
                updatehelp(mid + 1,se,i,diff,2*si + 2)
        if i < 0 or i > len(self.nums) - 1:
            return
        diff =  val - self.nums[i] 
        self.nums[i] = val
        updatehelp(0,len(self.nums)-1,i,diff,0)
