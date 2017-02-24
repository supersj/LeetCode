class Solution(object):
    x = 0

    def setable(self, i, j, p, tl, tr):
        return p[j] != 1 and tl[i + j] != 1 and tr[j - i + len(p) - 1] != 1

    def solveNQueensHelp(self, n, depth, p, tl, tr, result):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if depth == n:
            self.x += 1
        for j in range(n):
            if self.setable(depth, j, p, tl, tr):
                p[j] = 1
                tl[depth + j] = 1
                tr[j - depth + len(p) - 1] = 1
                result[depth] = j
                self.solveNQueensHelp(n, depth + 1, p, tl, tr, result)
                p[j] = 0
                tl[depth + j] = 0
                tr[j - depth + len(p) - 1] = 0

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        p = [0] * n
        result = [0] * n
        tl = [0] * (2 * n - 1)
        tr = [0] * (2 * n - 1)
        result = [0] * n
        self.solveNQueensHelp(n, 0, p, tl, tr, result)
        return self.x

hh = Solution


print(hh)