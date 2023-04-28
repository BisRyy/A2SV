class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] or grid[n-1][n-1]: return -1
        
        newpaths = [(0,0,1)]
        for path in newpaths:
            x, y, d = path
            if (x,y) == (n-1,n-1):
                return d

            if y < n - 1:
                if grid[x][y+1] == 0:
                    grid[x][y+1] = 1
                    newpaths.append((x,y+1,d+1))

                if x < n - 1:
                    if grid[x + 1][y+1] == 0:
                        grid[x+1][y+1] = 1
                        newpaths.append((x+1,y+1,d+1))

                if x > 0:
                    if grid[x - 1][y+1] == 0:
                        grid[x-1][y+1] = 1
                        newpaths.append((x-1,y+1,d+1))

            if x < n - 1:
                if grid[x + 1][y] == 0:
                    grid[x+1][y] = 1
                    newpaths.append((x+1,y,d+1))

                if y > 0:
                    if grid[x + 1][y-1] == 0:
                        grid[x+1][y-1] = 1
                        newpaths.append((x+1,y-1,d+1))

            if x > 0:
                if grid[x - 1][y] == 0:
                    grid[x-1][y] = 1
                    newpaths.append((x-1,y,d+1))

            if y > 0:
                if grid[x][y - 1] == 0:
                    grid[x][y-1] = 1
                    newpaths.append((x,y-1,d+1))

                if x > 0:
                    if grid[x - 1][y-1] == 0:
                        grid[x-1][y-1] = 1
                        newpaths.append((x-1,y-1,d+1))
        return -1
    