# the same as the minimum the cost of matrix multiply
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def max3(num3):
            a = num3[0]
            b = num3[1]
            c = num3[2]
            vb = a*b*c + a*c + max(a,c)
            va = a*b + b*c + max(b,c)
            vc = b*c + a*b + max(a,b)
            if va >= vb and va >= vc:
                return a*b,[b,c]
            elif vb >= va and vb >= vc:
                return a*b*c,[a,c]
            elif vc >= va and vc >= vb:
                return b*c,[a,b]
        def max4(num1,num2):
            nums = [1]+num1+num2+[1]
            maximum = 0
            value = 0
            result = num1
            for i in range(1,len(nums)-1):
                tmp = nums[i]*nums[i-1]*nums[i+1]
                tmpnum = nums[1:i]+nums[i+1:5]
                v,m = max3(tmpnum)
                if v+tmp+m[0]*m[1]+max(m) > maximum:
                    maximum = v+tmp+m[0]*m[1]+max(m)
                    value = v + tmp
                    result = m
                m = []
            return value,result
        nlen = len(nums)
        if nlen == 0:
            return 0
        if nlen == 1:
            return nums[0]
        if nlen == 2:
            return nums[0]*nums[1] + max(nums)
        m = [[[0,0] for i in range(nlen)] for j in range(nlen)]
        v = [[0]*nlen for j in range(nlen)]
        for i in range(0,nlen-1):
            m[i][i+1] = [nums[i],nums[i+1]]
            v[i][i+1] = 0
        for i in range(0,nlen-2):
            v[i][i+2],m[i][i+2] = max3(nums[i:i+3])
        for t in range(4,nlen+1):
            for i in range(0,nlen-t+1):
                maximum = 0
                value = 0
                result = [0,0]
                for j in range(i+2,i+t-1):
                    tmpv,tmpm = max4(m[i][j-1],m[j][i+t-1])
                    if tmpv + v[i][j-1] + v[j][i+t-1] + tmpm[0]*tmpm[1] + max(tmpm) > maximum:
                        maximum = tmpv + v[i][j-1] + v[j][i+t-1] + tmpm[0]*tmpm[1] + max(tmpm)
                        result = tmpm
                        value = tmpv + v[i][j-1] + v[j][i+t-1]
                m[i][i+t-1] = result
                v[i][i+t-1] = value
        return v[0][nlen-1] + m[0][nlen-1][0]*m[0][nlen-1][1] + max(m[0][nlen-1])

hh = Solution()
nums = [9,76,64,21,97,60,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,64,21,4,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21,76,64,21]
print(hh.maxCoins(nums))


class Solution1(object):
    def maxCoins(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for k in range(2, n):
            for left in range(0, n - k):
                right = left + k
                for i in range(left + 1, right):
                    dp[left][right] = max(dp[left][right],
                                          nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        return dp[0][n - 1]