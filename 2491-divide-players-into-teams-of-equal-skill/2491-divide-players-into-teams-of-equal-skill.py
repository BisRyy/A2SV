class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        
        '''
        skill = [3,2,5,1,3,4]
        sorted = [1,2,3,3,4,5]
        answer = (1, 5), (2, 4), (3, 3)
        
        '''
        n = len(skill)
        skill.sort()
        team = skill[0] + skill[-1]
        answer = 0
        for i in range(n//2):
            chemistry = skill[i] * skill[n-1-i]
            team_sum = skill[i] + skill[n-1-i]
            if team == team_sum:
                answer += chemistry
            else:
                return -1
        return answer
                
            