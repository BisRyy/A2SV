class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        def dfs(node, visited):
            print(node)
            if node == destination:
                return True
            
            visited.add(node)
            
            for neighbour in d[node]:
                if neighbour not in visited:
                    if dfs(neighbour, visited):
                        return True
                
            return False
        
        
        e  = len(edges)
        d = defaultdict(list)
        
        for edge in edges:
            d[edge[0]] += [edge[1]]
            d[edge[1]] += [edge[0]]
            
        print(d)
        
        visited = set()
        
        return dfs(source, visited)