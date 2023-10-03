class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        memo = {}
        
        def helper(i, t):
            if i == len(satisfaction):
                return 0
            
            if (i,t) in memo:
                return memo[(i,t)]
            
            memo[(i,t)] = max((satisfaction[i] * t) + helper(i+1, t+1), helper(i+1, t) )
            return memo[(i,t)]
        
        return helper(0,1)