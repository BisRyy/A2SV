class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        memo = [0] * (len(triangle)+1)
        
        for row in triangle[::-1]:
            for i in range(len(row)):
                memo[i] = row[i] + min(memo[i], memo[i+1])
                
        return memo[0]