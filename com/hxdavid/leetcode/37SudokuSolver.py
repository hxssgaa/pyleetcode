from time import clock


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.solve(board, 0)

    def solve(self, board, pos):
        """
        :type board: list[list[str]]
        :type pos: 0
        :rtype: bool
        """
        if pos >= 81:
            return True
        i, j = pos // 9, pos % 9
        if board[i][j] == '.':
            for c in range(1, 10):  # Trial. Try 1 through 9 for each cell
                if self.isValid(board, i, j, c):
                    board[i][j] = str(c)  # Put c for this cell
                    if self.solve(board, pos + 1):  # If it's the solution return true
                        return True
                    else:
                        board[i][j] = '.'  # Otherwise go back
            return False
        return self.solve(board, pos + 1)

    def isValid(self, board, i, j, c):
        """
        :type board: list[list[str]]
        :type i: int
        :type j: int
        :type c: int
        :rtype: bool
        """
        c = str(c)
        # Check column
        for row in range(9):
            if board[row][j] == c:
                return False
        # Check row
        for col in range(9):
            if board[i][col] == c:
                return False
        # Check 3 x 3 block
        for row in range((i // 3) * 3, (i // 3) * 3 + 3):
            for col in range((j // 3) * 3, (j // 3) * 3 + 3):
                if board[row][col] == c:
                    return False
        return True


input_str = [".........", "7........", ".2.......", "..7...24.", ".64.1....", ".9....3..", "...8.3...", "........6",
             "...2759.."]
board = [[input_str[i][j] for j in range(9)] for i in range(9)]
start = clock()
Solution().solveSudoku(board)
end = clock()
print("costs:" + str(end - start))
for l in board:
    for x in l:
        print(x, end=' ')
    print()
