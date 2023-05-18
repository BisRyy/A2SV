class unionfind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.score = [float('inf') for i in range(n)]

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def unite(self, i, j, k):
        self.score[i] = min(self.score[i], k)
        self.score[j] = min(self.score[j], k)
        i = self.find(i)
        j = self.find(j)
        if i != j:
            self.parent[i] = j

    def issame(self, i, j):
        return self.find(i) == self.find(j)

    def groups(self):
        r = range(len(self.parent))
        return [set([j for j in r if self.issame(j, i)]) for i in r if i == self.parent[i]]
    
class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        u = unionfind(n+1)
        for x, y, z in roads:
            u.unite(x,y,z)
        ans = float('inf')
        f = u.find(1)
        for x, y, z in roads:
            if f == u.find(x) == u.find(y):
                ans =  min(ans, z)
        return ans
        