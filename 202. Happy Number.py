class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashmap = {}
        remain = 0
        squareSum = 0
        while not hashmap.has_key(n):
            hashmap[n] = 1
            squareSum = 0
            while n > 0:
                remain = n % 10
                squareSum += remain*remain
                n //= 10
            if squareSum == 1:
                return True
            else:
                n = squareSum
        return False


