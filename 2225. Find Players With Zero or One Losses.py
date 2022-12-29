class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans = [[],[]]
        
        loses = defaultdict(int)
        
        for player in matches:
            loses[player[0]] = 0
            
        for player in matches:
            loses[player[1]] += 1
                        
        for loser in loses.keys():
            if loses[loser] == 0:
                ans[0].append(loser)
            
            elif loses[loser] == 1:
                ans[1].append(loser)
            
        ans[0].sort()
        ans[1].sort()
        return ans            
