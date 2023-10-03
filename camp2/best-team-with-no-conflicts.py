class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        pairs = [[scores[i], ages[i]] for i in range(len(ages))]
        pairs.sort()
        
        memo = [pairs[i][0] for i in range(len(scores))]
        
        
        for i in range(1,len(scores)):
            for j in range(i-1,-1,-1):
                if pairs[j][1] <= pairs[i][1]:
                    memo[i] = max(memo[i], pairs[i][0] + memo[j])
                    
        return max(memo)