class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        indeg=[0]*n
        adj=[[] for i in range(n)]
        for i in range(n):
            indeg[i]=len(graph[i])
            for j in graph[i]:
                adj[j].append(i)
                
        q=deque()
        res=[]*n
        for i in range(n):
            if indeg[i]==0:
                q.append(i)
                
        while q:
            u=q.popleft()
            res.append(u)
            for i in adj[u]:
                if indeg[i]!=0:
                    indeg[i]-=1
                if indeg[i]==0:
                    q.append(i)
                    
        return sorted(res)