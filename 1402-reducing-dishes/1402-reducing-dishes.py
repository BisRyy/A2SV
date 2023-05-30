class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        ans = 0
        for i in range(len(satisfaction)):
            tot = 0
            for j in range(len(satisfaction[i:])):
                tot += satisfaction[i:][j] * (j + 1)
                
            ans = max(tot, ans)
            
        return ans
                