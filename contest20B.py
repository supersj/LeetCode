class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(n,num):
            if n <= 0:
                return 1
            count = 0
            for i in range(n):
                if num[i] % n == 0 or n % num[i] == 0:
                    num[i],num[n-1] = num[n-1],num[i]
                    count += helper(n-1,num)
                    num[i],num[n-1] = num[n-1],num[i]
            return count
        num = [i+1 for i in range(N)]
        return helper(N,num)
N = 4
hh = Solution()
print(hh.countArrangement(N))

