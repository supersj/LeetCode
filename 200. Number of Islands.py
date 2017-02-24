# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# 11110
# 11010
# 11000
# 00000
# Answer: 1
#
# Example 2:
#
# 11000
# 11000
# 00100
# 00011
# Answer: 3
#
# Credits:
# Special thanks to @mithmatt for adding this problem and creating all test cases.
#
# Subscribe to see which companies asked this question

# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# For example,
# X X X X
# X O O X
# X X O X
# X O X X
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X
# TODO solution is very brilliant
# TODO and this problem can be also solved by union find


class Solution1(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        row = len(board)
        if not row:
            return
        col = len(board[0])
        for i in range(row):
            self.check(board,i,0,row,col)
            if col>1:
                self.check(board,i,col-1,row,col)
        for j in range(1,col-1):
            self.check(board,0,j,row,col)
            if row>1:
                self.check(board,row-1,j,row,col)
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
        for i in range(row):
            for j in range(col):
                if board[i][j] == '1':
                    board[i][j] = 'O'

    def check(self,board,i,j,row,col):
        if board[i][j] == 'O':
            board[i][j] = '1'
            if i>1:
                self.check(board,i-1,j,row,col)
            if j>1:
                self.check(board,i,j-1,row,col)
            if i+1<row:
                self.check(board,i+1,j,row,col)
            if j+1<col:
                self.check(board,i,j+1,row,col)


class Solution(object):
    def numIslands(self, board):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        board = [[e for e in ele] for ele in board]

        def check(board,i, j, row, col):
            if  i<0 or j<0 or i>=row or j>=col or board[i][j] != '1':
                return
            board[i][j] = '0'
            check(board, i - 1, j, row, col)
            check(board, i, j - 1, row, col)
            check(board, i + 1, j, row, col)
            check(board, i, j + 1, row, col)

        def check1( board, i, j, row, col):
            if board[i][j] == '0':
                return
            board[i][j] = '0'
            if i >=1:
                check1(board, i - 1, j, row, col)
            if j >=1:
                check1(board, i, j - 1, row, col)
            if i + 1 < row:
                check1(board, i + 1, j, row, col)
            if j + 1 < col:
                check1(board, i, j + 1, row, col)
        count = 0
        row = len(board)
        col = 0
        if row >= 1:
            col = len(board[0])
        for i in range(row):
            for j in range(col):
               if  board[i][j] == '1':
                   count += 1
                   check1(board,i,j,row,col)
        return count
hh = Solution()
board = ["111","010","111"]
print(hh.numIslands(board))