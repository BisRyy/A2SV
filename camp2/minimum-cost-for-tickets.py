class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        
        def helper(i):
            if i ==  len(days):
                return 0
            if i in memo:
                return memo[i]
            
            ans = float("inf")
            
            j = i
            while j < len(days) and days[j] < days[i] + 1:
                j+=1
            ans = min(ans, costs[0] + helper(j))
            
            j = i
            while j < len(days) and days[j] < days[i] + 7:
                j+=1
            ans = min(ans, costs[1] + helper(j))
            
            j = i
            while j < len(days) and days[j] < days[i] + 30:
                j+=1
            ans = min(ans, costs[2] + helper(j))
            
            memo[i] = ans
            return memo[i]
            
           
        return helper(0)
            