class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs)
        
        @cache
        def dfs(i, a, b):
            if a == b == n // 2:
                return 0
            if i >= n:
                return math.inf
            if a > n//2 or b > n // 2:
                return math.inf
            x =  costs[i][0] + dfs(i+1, a+1, b)
            y =  costs[i][1] + dfs(i+1, a, b+1)
            return min(x, y)
        
        return dfs(0,0,0)
            
        
            