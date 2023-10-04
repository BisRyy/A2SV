class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        for x, y ,z in  times:
            graph[x].append((y, z))
            
        def dijkstra(graph, start):
            
            distances = {}
            distances[start] = 0
            visited = set()
            heap = [(0, start)]
            while heap:
                distance, node = heappop(heap)
                
                if node in visited:
                    continue
                visited.add(node)
                
                for child, dis in graph[node]:
                    if dis + distance < distances.setdefault(child, inf):
                        distances[child] = dis + distance
                        heappush(heap, ( dis + distance, child))
            
            if len(visited) == n:
                return max(distances.values())
            return -1
        
        return dijkstra(graph, k)
            
            