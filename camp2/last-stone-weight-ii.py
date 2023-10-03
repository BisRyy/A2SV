class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = ceil(sum(stones)/2)
        
        def helper(i, total):
            if target <= total or i == len(stones):
                return abs(total - (sum(stones) - total))
            
            if (i, total) in memo:
                return memo[(i, total)] 
            
            memo[(i, total)] = min(helper(i+1, total), helper(i+1, total+ stones[i]))
            return memo[(i, total)] 
        
        memo = {}
        return helper(0,0)