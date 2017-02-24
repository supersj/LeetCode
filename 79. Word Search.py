# Given a 2D board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
#
# For example,
# Given board =
#
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# word = "ABCCED", -> returns true,
# word = "SEE", -> returns true,
# word = "ABCB", -> returns false.

class Solution(object):
    def exist(self, board, word):
        n = 0
        m = len(board)
        if m >= 1:
            n = len(board[0])
        if m == 0 and len(word) != 0:
            return False
        if len(word) == 0:
            return True
        visited = [[False for i in range(n)] for j in range(m)]
        points = self.starts(board, word, m, n)
        for point in points:
            row = point[0]
            column = point[1]
            start = 0
            if self.dfs(row, column, board, visited, word, start, m, n):
                return True
        return False

    def starts(self, board, word, m, n):
        points = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    points.append((i, j))
        return points

    def nextable(self, row, column, visited, board, ele, m, n):
        if row >= m or row < 0 or column >= n or column < 0:
            return False
        if visited[row][column] == True:
            return False
        if board[row][column] != ele:
            return False
        return True

    def dfs(self, row, column, board, visited, word, start, m, n):
        visited[row][column] = True
        start += 1
        if start == len(word):
            return True
        for t in range(4):
            i, j = self.myIter(row, column, t)
            if self.nextable(i, j, visited, board, word[start], m, n):
                if self.dfs(i, j, board, visited, word, start, m, n):
                    return True
                visited[i][j] = False
        visited[row][column] = False
        return False

    def myIter(self, row, column, number):
        if number == 0:
            return row - 1, column
        if number == 1:
            return row, column + 1
        if number == 2:
            return row + 1, column
        if number == 3:
            return row, column - 1
