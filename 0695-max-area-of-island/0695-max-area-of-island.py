class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(vertical, horizontal, area):
            grid[vertical][horizontal] = 0
            self.max_area = max(self.max_area, area)
            
            if vertical+1 < m and grid[vertical+1][horizontal] == 1:
                area = dfs(vertical+1, horizontal, area+1)
                
            if vertical-1 >= 0 and grid[vertical-1][horizontal] == 1:
                area = dfs(vertical-1, horizontal, area+1)
                
            if horizontal+1 < n and grid[vertical][horizontal+1] == 1:
                area = dfs(vertical, horizontal+1, area+1)
                
            if horizontal-1 >= 0 and grid[vertical][horizontal-1] == 1:
                area = dfs(vertical, horizontal-1, area+1)
                
            return area

        self.max_area = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i, j, 1)
        return self.max_area