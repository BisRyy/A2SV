class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        
        players.sort(reverse=True)
        trainers.sort(reverse=True)
        m, n = len(players), len(trainers)
        c = 0
        j = i = 0
        
        while i < m and j < n:
            if players[i] > trainers[j]:
                i+=1
            else:
                i+=1
                j+=1
                c+=1
            
        return c