class Solution1(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # Dynamic Programming implementation of LCS problem

        def lcs(X, Y):
            # find the length of the strings
            m = len(X)
            n = len(Y)

            # declaring the array for storing the dp values
            L = [[0] * (n + 1) for i in range(m + 1)]

            """Following steps build L[m+1][n+1] in bottom up fashion
            Note: L[i][j] contains length of LCS of X[0..i-1]
            and Y[0..j-1]"""
            for i in range(m + 1):
                for j in range(n + 1):
                    if i == 0 or j == 0:
                        L[i][j] = 0
                    elif X[i - 1] == Y[j - 1]:
                        L[i][j] = L[i - 1][j - 1] + 1
                    else:
                        L[i][j] = max(L[i - 1][j], L[i][j - 1])

            # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
            return L[m][n]

        # end of function lcs
        tmp = list(set(nums))
        tmp.sort()
        return lcs(nums,tmp)

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def ceilIndex(A,l,r,key):
            while r-l > 1:
                m = l + (r - l)//2
                if A[m] >= key:
                    r = m
                else:
                    l = m
            return r
        if not nums:
            return 0
        tail = [nums[0]]
        l = 1
        for i in range(1,len(nums)):
            if nums[i] < tail[0]:
                tail[0] = nums[i]
            elif nums[i] > tail[-1]:
                tail.append(nums[i])
                l+=1
            else:
                tail[ceilIndex(tail,-1,l-1,nums[i])] = nums[i]
        return l
nums = [10,9,2,5,3,7,101,18]
hh = Solution()
print(hh.lengthOfLIS(nums))