
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        # ans = []
        onesrow,onescol = [],[]
        for i in range(len(grid[0])):
            onesCol = 0
            for j in range(len(grid)):
                onesCol += 1 if grid[j][i] else 0
            onescol.append(onesCol)
        for row in grid:
            onesrow.append(sum(row))
        
        for i,row in enumerate(onesrow):
            for j,col in enumerate(onescol):
                grid[i][j] = row + col - (len(grid[0]) - row) - (len(grid) - col)
                
        return grid