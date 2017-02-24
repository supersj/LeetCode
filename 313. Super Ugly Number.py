import sys
import heapq
class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dp = [1]*n
        idx = [0]*len(primes)
        for i in range(1,n):
            dp[i] = sys.maxsize
            dp[i] = min([dp[idx[j]]*primes[j] for j in range(len(primes))])
            for j in range(len(primes)):
                if dp[i] == dp[idx[j]]*primes[j]:
                    idx[j]+=1
        return dp[-1]

    def nthSuperUglyNumber1(self, n, primes):
        uglies = [1]

        def gen(prime):
            for ugly in uglies:
                yield ugly * prime
        ll = map(gen, primes)
        print(*ll)
        merged = heapq.merge(*map(gen, primes))
        print(type(merged))
        while len(uglies) < n:
            ugly = next(merged)
            print(ugly)
            if ugly != uglies[-1]:
                uglies.append(ugly)
        return uglies[-1]
n = 4
primes = [2,3,5]
hh = Solution()
print(hh.nthSuperUglyNumber1(n,primes))
