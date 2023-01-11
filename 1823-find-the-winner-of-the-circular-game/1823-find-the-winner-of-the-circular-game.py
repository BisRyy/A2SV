class Solution:
    def findTheWinner(self, n: int, k: int) -> int:

        players = [num for num in range(1, n+1)]
        
        current = 0
        k = k-1
        for round in range(len(players) - 1):
            current += k
            current %= n 
            players.remove(players[current])
            n -= 1
            
        return players[0]