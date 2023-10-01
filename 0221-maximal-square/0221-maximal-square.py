class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        
        memo = [[0]*(c+1) for i in range(r+1)]
        ans = 0
        
        for x in range(r-1, -1, -1):
            for y in range(c-1, -1, -1):
                bottom =  memo[x+1][y]
                right =  memo[x][y+1]           
                diagonal =  memo[x+1][y+1]    

                if matrix[x][y] == "1":
                    memo[x][y] = 1 + min(bottom, right, diagonal)
                ans = max(ans, memo[x][y])
        return ans**2