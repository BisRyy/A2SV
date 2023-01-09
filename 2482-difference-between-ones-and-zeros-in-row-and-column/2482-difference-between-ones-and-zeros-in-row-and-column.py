
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        ones = [[],[]] # row, column
        
        for i in range(n):
            _sum = 0
        
            for j in range(m):
                _sum += 1 if grid[j][i] else 0
                
            ones[1].append(_sum)
            
        for row in grid:
            ones[0].append(sum(row))
        
        for i,row in enumerate(ones[0]):
                
            for j,col in enumerate(ones[1]):
                grid[i][j] = 2*(row + col) - n - m 
                
        return grid