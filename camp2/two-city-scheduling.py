class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        @cache
        def dfs(i, a, b):
            if i == n:
                if a != b:
                    return math.inf
                return 0
            x, y = 0, 0
            
            if a < n:
                x = costs[i][0] + dfs(i+1, a+1, b)
            if b < n:
                y = costs[i][1] + dfs(i+1 , a, b+1)
            
            return min(x, y)
        
        return dfs(0,0,0)
            
        
            