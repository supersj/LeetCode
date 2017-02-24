import copy
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        tmpboard = copy.deepcopy(board)
        row = len(tmpboard)
        col = 0
        if row > 0:
            col = len(tmpboard[0])
        tmpboard.insert(0,[0]*col)
        tmpboard.append([0]*col)
        for rowele in tmpboard:
            rowele.append(0)
            rowele.insert(0,0)
        def cnt(i,j,board):
            return board[i-1][j-1] + board[i-1][j] + board[i-1][j+1]\
                   + board[i][j-1] + board[i][j+1] + board[i+1][j-1]\
                   + board[i+1][j] + board[i+1][j+1]
        for i in range(1,row+1):
            for j in range(1,col+1):
                cntlive = cnt(i,j,tmpboard)
                islive = board[i-1][j-1]
                if islive:
                    if cntlive < 2:
                        board[i-1][j-1] = 0
                        continue
                    elif 2<=cntlive<=3:
                        continue
                    else:
                        board[i-1][j-1] = 0
                else:
                    if cntlive == 3:
                        board[i-1][j-1] = 1
                    else:
                        continue


"""
public void gameOfLife(int[][] board) {
    if (board == null || board.length == 0) return;
    int m = board.length, n = board[0].length;

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int lives = liveNeighbors(board, m, n, i, j);

            // In the beginning, every 2nd bit is 0;
            // So we only need to care about when will the 2nd bit become 1.
            if (board[i][j] == 1 && lives >= 2 && lives <= 3) {
                board[i][j] = 3; // Make the 2nd bit 1: 01 ---> 11
            }
            if (board[i][j] == 0 && lives == 3) {
                board[i][j] = 2; // Make the 2nd bit 1: 00 ---> 10
            }
        }
    }

    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            board[i][j] >>= 1;  // Get the 2nd state.
        }
    }
}

public int liveNeighbors(int[][] board, int m, int n, int i, int j) {
    int lives = 0;
    for (int x = Math.max(i - 1, 0); x <= Math.min(i + 1, m - 1); x++) {
        for (int y = Math.max(j - 1, 0); y <= Math.min(j + 1, n - 1); y++) {
            lives += board[x][y] & 1;
        }
    }
    lives -= board[i][j] & 1;
    return lives;
}
"""