class UnionFind:
    def __init__(self, n):
        self.par = [i for i in range(n)]
        self.rank = [1] * n
    
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)
        if p1 != p2:
            if self.rank[p1] >= self.rank[p2]:
                self.rank[p1] += self.rank[p2]
                self.par[p2] = p1
                return self.rank[p1]
            else:
                self.rank[p2] += self.rank[p1]
                self.par[p1] = p2
                return self.rank[p2]
    
    def find(self, n):
        if self.par[n] == n:
            return n
        self.par[n] = self.find(self.par[n])
        return self.par[n]

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n, h = len(points), []
        
        for i in range(n):
            for j in range(i + 1, n):
                dis = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(h, [dis, i, j])
                
        uf, cost = UnionFind(n), 0
        while uf.rank[0] != n:
            dis, n1, n2 = heapq.heappop(h)
            if uf.find(n1) != uf.find(n2):
                size = uf.union(n1, n2)
                cost += dis
                if size == n:
                    break
        return cost