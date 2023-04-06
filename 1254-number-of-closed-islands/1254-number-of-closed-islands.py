class UnionFind:
    def __init__(self, n):
        self.parents = list(range(n))
        self.ranks = [0] * n
    
    def find(self, i):
        if self.parents[i] != i: self.parents[i] = self.find(self.parents[i])
        return self.parents[i]
    
    def merge(self, i, j):
        ri, rj = self.find(i), self.find(j)
        if ri != rj:
            if self.ranks[ri] == self.ranks[rj]:
                self.parents[ri] = rj
                self.ranks[rj] += 1
            elif self.ranks[ri] < self.ranks[rj]:
                self.parents[ri] = rj
            else:
                self.parents[rj] = ri

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        def map(r, c): return r * n + c

        union_find = UnionFind(m * n)
        island_count = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    island_count += 1
                    for ir, ic in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                        rr, cc = r + ir, c + ic
                        if 0 <= rr < m and 0 <= cc < n and grid[rr][cc] == 0:
                            if union_find.find(map(r, c)) != union_find.find(map(rr, cc)):
                                island_count -= 1
                                union_find.merge(map(r, c), map(rr, cc))
        
        open_islands = set()
        for r in range(m):
            if grid[r][0] == 0:
                open_islands.add(union_find.find(map(r, 0)))
            if grid[r][n - 1] == 0:
                open_islands.add(union_find.find(map(r, n - 1)))
        for c in range(n):
            if grid[0][c] == 0:
                open_islands.add(union_find.find(map(0, c)))
            if grid[m - 1][c] == 0:
                open_islands.add(union_find.find(map(m - 1, c)))

        return island_count - len(open_islands)