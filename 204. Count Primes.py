class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TODO why 0 or 1 is better than True or False
        prime = [True for i in range(n)]
        for i in range(2,n):
            if i*i >n:
                break
            if not prime[i]:
                continue
            for j in range(i*i,n,i):
                prime[j] = False
        count = 0
        for i in range(2,n):
            if prime[i]:
                count += 1
        return count