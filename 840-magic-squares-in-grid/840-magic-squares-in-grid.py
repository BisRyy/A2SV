class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        d = {}
        c = 0
        for x in range(1,10): 
            d[x] = 0
            
        for i in range(m - 2):
            for j in range(n - 2):
                    
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        if grid[row][col] in d:
                            d[grid[row][col]] += 1
                        
                f = True
                for x in d:
                    if d[x] != 1:
                        f = False
                        break
                    
                if f and grid[i][j] + grid[i][j+1] + grid[i][j+2] == grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] == grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] == grid[i][j] + grid[i+1][j] + grid[i+2][j] ==  grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] ==  grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] ==  grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] ==  grid[i+2][j] + grid[i+1][j+1] + grid[i][j+2]: c +=1 
                
                for x in d:
                    d[x] = 0
        return c
