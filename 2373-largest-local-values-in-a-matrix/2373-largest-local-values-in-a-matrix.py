class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid) - 2
        maxLocal = [[0]*n for _ in range(n)]
        
        for row in range(1, len(grid) -1):
            
            for col in range(1, len(grid[0]) -1 ):
                largest = 0

                for i in range(row - 1, row + 2):
                    
                    for j in range(col -  1, col + 2):
                        largest = max(grid[i][j], largest)
                        
                maxLocal[row - 1][col - 1] = largest
        
        return maxLocal