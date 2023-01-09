# class Solution:
#     def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
#         m = len(grid)
#         n = len(grid[0])
#         ones = [[],[]] # row, column
        
#         for column in range(n):
#             _sum = 0
#             for row in range(m):
#                 # ones[0].append(sum(grid[row]))
#                 _sum += grid[row][column]
#             ones[1].append(_sum)
            
        
#         for row in range(m):
#             ones[0].append(sum(grid[row]))
            
#         for row in ones[0]:
#             temp = []
#             for col in ones[1]:
#                 temp.append(row*2 + col - n - m + col *2)
#             grid[row] = temp
#         return grid
        
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        ones = [[],[]] # row, column
        for i in range(len(grid[0])):
            onesCol = 0
            for j in range(len(grid)):
                onesCol += 1 if grid[j][i] else 0
            ones[1].append(onesCol)
            
        for row in grid:
            ones[0].append(sum(row))
        
        for i,row in enumerate(ones[0]):
            for j,col in enumerate(ones[1]):
                grid[i][j] = row + col - (len(grid[0]) - row) - (len(grid) - col)
                
        return grid