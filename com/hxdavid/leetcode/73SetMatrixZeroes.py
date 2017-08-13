class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        m, n, first_row_has_zero = len(matrix), len(matrix[0]), not all(matrix[0])
        # Use matrix[0][j] and matrix[i][0] as marker zero.
        for i in range(1, m):
            for j in range(0, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = matrix[i][0] = 0
                    print_matrix(matrix)
        # After first row and column marked zero, we can determine if matrix[i][j] would be zero.
        for i in range(m - 1, 0, -1):
            for j in range(n - 1, -1, -1):
                if matrix[0][j] == 0 or matrix[i][0] == 0:
                    matrix[i][j] = 0
                    print_matrix(matrix)
        if first_row_has_zero:
            matrix[0] = [0] * n


def print_matrix(matrix):
    print()
    for row in matrix:
        print(" ".join(str(p) for p in row))


matrix = [[1, 2, 3, 0], [4, 1, 0, 2], [2, 0, 7, 8], [1, 2, 3, 4]]
print_matrix(matrix)
Solution().setZeroes(matrix)
print_matrix(matrix)
