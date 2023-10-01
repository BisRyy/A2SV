class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        r, c = len(matrix), len(matrix[0])
        
        memo = {}
        
        
        def helper(x, y):
            if x >= r or y >= c:
                return 0
            
            if (x, y) in memo:
                return memo[(x, y)]
            
            bottom =  helper(x+1, y)
            right =  helper(x, y+1)            
            diagonal =  helper(x+1, y+1)    
            
            if matrix[x][y] == "1":
                memo[(x, y)] = 1 + min(bottom, right, diagonal)
            else:
                memo[(x,y)] = 0
            
            return memo[(x, y)]
            
        helper(0,0)
        return max(memo.values())**2