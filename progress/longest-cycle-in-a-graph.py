class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def dfs(node, t=0):
            if node in visited or edges[node] == -1:
                return -1
            if time[node] < t:
                return t - time[node]
            time[node] = t
            res = dfs(edges[node], t + 1)
            visited.add(node)
            return res
        
        N = len(edges)
        visited = set()
        time = [N] * N        
        return max(dfs(i) for i in range(N))