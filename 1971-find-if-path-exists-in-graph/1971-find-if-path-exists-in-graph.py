class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        visited = set()
        def dfs(node):
            print(node)
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbour in d[node]:
                if neighbour not in visited:
                    if dfs(neighbour):
                        return True
            return False
        
        d = defaultdict(list)
        for edge in edges:
            d[edge[0]] += [edge[1]]
            d[edge[1]] += [edge[0]]
        
        return dfs(source)