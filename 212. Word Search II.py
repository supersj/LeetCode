class TrieNode(object):
    def __init__(self):
        self.val = None
        self.next = {}
class Solution(object):
    def __init__(self):
        self.ans = []

    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """

        def build(words):
            root = TrieNode()
            for word in words:
                node = root
                for c in word:
                    if c not in node.next.keys():
                        node.next[c] = TrieNode()
                    node = node.next[c]
                node.val = word[:]
            return root

        def backtrack(board, i, j,row,col, node):
            c = board[i][j]
            if c == '#' or not node.next.has_key(c):
                return
            node = node.next[c]
            if node.val:
                self.ans.append(node.val)
                node.val = None
            board[i][j] = '#'
            if (i > 0): backtrack(board, i - 1, j,row,col, node);
            if (j > 0): backtrack(board, i, j - 1,row, col, node);
            if (i + 1 < row): backtrack(board, i + 1, j,row,col, node);
            if (j + 1 < col): backtrack(board, i, j + 1,row,col, node);
            board[i][j] = c

        row = len(board)
        col = 0
        if row >0 :
            col = len(board[0])
        root = build(words)
        board = [[e for e in ele]for ele in board]
        for i in range(row):
            for j in range(col):
                backtrack(board, i, j, row, col, root)
        return self.ans
hh = Solution()
board = ["oaan","etae","ihkr","iflv"]
words = ["oath","pea","eat","rain"]
hh.findWords(board,words)