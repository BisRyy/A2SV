class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        
        neighbors = defaultdict(set)
        for a, b in roads:
            neighbors[a].add(b)
            neighbors[b].add(a)
            
        ans = 0

        def traverse(node, parent) -> int:
            
            nonlocal ans
            passengers = 1 + sum(traverse(n, node) for n in neighbors[node] if n != parent)
            
            if node != 0:
                ans += ceil(passengers / seats)
                
            return passengers

        traverse(0, -1)
        return ans