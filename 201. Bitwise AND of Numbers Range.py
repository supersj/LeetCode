class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        step = 0
        while m!= n:
            m >>= 1
            n >>= 1
            step+=1
        return m<<step