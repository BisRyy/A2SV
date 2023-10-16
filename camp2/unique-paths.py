class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[1 for j in range(n)] for i in range(m)]
        for j in range(1, n):
            for i in range(1,m):
                matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
        return matrix[m-1][n-1]