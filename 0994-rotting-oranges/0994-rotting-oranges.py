class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        
        c = 0
        d = 0
        rotten = []
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    c+=1
                elif grid[i][j] == 2:
                    rotten.append((i,j))
                    d+=1
                    
        if c == 0:
            return 0
        queue = deque(rotten)
        v = set()
        time = 0
        
        while queue:            
            q = deque()
            for popped in queue:
                if popped in v:
                    continue
                if popped[0] < m - 1:
                    if grid[popped[0] + 1][popped[1]] == 1:
                        grid[popped[0] + 1][popped[1]] = 2
                        q.append((popped[0] + 1, popped[1]))
                        c -= 1
                if popped[1] < n - 1:
                    if grid[popped[0]][popped[1] + 1] == 1:
                        grid[popped[0]][popped[1] + 1] = 2
                        q.append((popped[0], popped[1] + 1))
                        c -= 1
                if popped[0] > 0:
                    if grid[popped[0] - 1][popped[1]] == 1:
                        grid[popped[0] - 1][popped[1]] = 2
                        q.append((popped[0] - 1, popped[1]))
                        c -= 1
                if popped[1] > 0:
                    if grid[popped[0]][popped[1] - 1] == 1:
                        grid[popped[0]][popped[1] - 1] = 2
                        q.append((popped[0], popped[1] - 1))
                        c -= 1
                v.add(popped)
            queue = q
            time+=1
        return time - 1 if c == 0  else -1 
                