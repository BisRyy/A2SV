class Union:
    def __init__(self, n):
        self.root = list(range(n))
        self.rank = [1] * n
        
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                root_x, root_y = root_y, root_x
            self.rank[root_y] += self.rank[root_x]
            self.root[root_x] = root_y
        
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        u = Union(n)
        for x, y in edges:
            u.union(x, y)
        return u.find(source) == u.find(destination)