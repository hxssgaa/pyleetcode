class Solution(object):
    def dfs(self, board, word, idx, i, j):
        """
        :type board: list[list[str]]
        :type word: str
        :type idx: int
        :type i: int
        :type j: int
        :rtype: bool
        """
        if idx == len(word):
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        t = board[i][j]
        board[i][j] = '#'  # A simple trick to mark the board with "#" instead of using visited matrix.
        res = self.dfs(board, word, idx + 1, i + 1, j) or \
              self.dfs(board, word, idx + 1, i - 1, j) or \
              self.dfs(board, word, idx + 1, i, j + 1) or \
              self.dfs(board, word, idx + 1, i, j - 1)
        board[i][j] = t
        return res

    def exist(self, board, word):
        """
        :type board: list[list[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not board[0]:
            return False
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                if c == word[0]:
                    if self.dfs(board, word, 0, i, j):
                        return True
        return False


# print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(Solution().exist([["a", "b", "c", "d", "e"],
                        ["b", "c", "d", "e", "f"],
                        ["c", "d", "e", "f", "g"],
                        ["h", "i", "j", "k", "l"],
                        ["z", "x", "a", "b", "c"]], "bkfejaxzhidcbabcdede"))
