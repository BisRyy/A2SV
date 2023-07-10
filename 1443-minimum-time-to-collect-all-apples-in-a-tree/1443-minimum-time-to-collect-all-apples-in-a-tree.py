class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adj = {i:[] for i in range(n)}
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            
        def dfs(node, par):
            time = 0
            for nei in adj[node]:
                if nei != par:
                    child = dfs(nei, node)
                    if child or hasApple[nei]:
                        time += 2 + child
            return time
        return dfs(0, -1)