class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        n = 0
        m = len(matrix)
        if m > 0:
            n = len(matrix[0])
        num = m + n -1
        result = []
        nlen = min(m,n)
        for i in range(num):
            if i % 2 == 0:
                times = 0
                right = 0
                row = i
                if i  > m - 1:
                    right = i - times - m + 1
                    row = m - 1
                while times < nlen and times <= i and times < (num - i):
                    result.append(matrix[row-times][times + right])
                    times += 1
            else:
                times = 0
                hight = 0
                col = i
                if i  > n - 1:
                    hight = i  - n + 1
                    col = n - 1
                while times < nlen and times <= i and times < (num - i):
                    result.append(matrix[times + hight][col-times])
                    times += 1
        return result

matrix = [[1,2,3,0]]
hh = Solution()
print(hh.findDiagonalOrder(matrix))