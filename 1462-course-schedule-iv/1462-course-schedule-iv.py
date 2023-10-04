class Solution:
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j in prerequisites:
            dist[i][j]  = 1
        for i in range(n):
            dist[i][i] = 0
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        ans = []
        for a, b in queries:
            ans.append(dist[a][b] != float("inf"))
        return ans
            
