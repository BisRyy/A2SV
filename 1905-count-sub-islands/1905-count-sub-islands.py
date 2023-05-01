class Solution:
    def countSubIslands(self, back: List[List[int]], grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        
        res = 0
        flag = True
        
        def dfs(i,j):
            nonlocal flag
            if grid[i][j]==1:
                if back[i][j] != 1:
                    flag = False
                grid[i][j]=0
                if j<n-1:
                    dfs(i,j+1)
                if j>0:
                    dfs(i,j-1)
                if i>0:
                    dfs(i-1,j)
                if i<m-1:
                    dfs(i+1,j)
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    
                    flag = True
                    dfs(i,j)
                    if flag :
                        res+=1
                    

        return res