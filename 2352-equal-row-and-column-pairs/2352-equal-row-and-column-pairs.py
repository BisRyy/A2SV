class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        a = []
        
        # rotate the colums
        for i in range(len(grid)):
            t = []
            for j in range(len(grid)):
                t.append(grid[j][i])
            a.append(t)
        count = 0
        
        # compare the arrays
        for i in range(len(a)):
            for j in range(len(grid)):
                
                same = False
                for k in range(len(grid)):
                    
                    if grid[i][k] == a[j][k]:
                        same = True
                    else:
                        same = False
                        break
                if same: 
                    count += 1
        return count