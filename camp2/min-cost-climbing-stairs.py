class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        cost.append(0)
        memo={}
        def dp(i,n):
            if i >= n: return 0
            if i in memo: return memo[i]
            memo[i] = cost[i] + min(dp(i+1, n), dp(i+2,n))
            return memo[i]
        
        return dp(-1, n)