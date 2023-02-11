class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        
        R, B, Gray = 0, 1, 2
        G = defaultdict(list)
        
        for v, w in redEdges:
            G[v].append((w,R))
            
        for v, w in blueEdges:
            G[v].append((w,B))
            
        que = deque([(0,0,Gray)])
        visited = set()
        res = [-1]*n
        dist = defaultdict(int)
        
        while que:
            d, v, vcolor = que.popleft()
            
            if (v, vcolor) in visited: 
                continue
                
            visited.add((v,vcolor))
            
            if v not in dist: 
                dist[v] = d
                
            res[v] = dist[v]
            
            for w, color in G[v]:
                
                if vcolor != color:
                    que.append((d+1, w, color))
                    
        return res