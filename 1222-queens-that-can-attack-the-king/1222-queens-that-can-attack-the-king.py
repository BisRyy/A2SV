class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        
        board = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0]
        ]
        attackers = []
        
                
        for queen in queens:
            board[queen[0]][queen[1]] = 1
        
        x = king[0]
        y = king[1]
        board[x][y] = 2
        
        # print(board)
        i, j = x , y
        
        #Up
        while i >= 0:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            i-=1
        
        i, j = x , y
        #Down
        while i < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                print([i,j])
                break
            i+=1
        
        i, j = x , y
        #right        
        while j < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                print([i,j])
                break
            j+=1
        
        i, j = x , y
        #left                  
        while j >= 0:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            j-=1
        
        i, j = x , y
        #diagonal top left
        while j >= 0 and j < 8 and i >= 0 and i < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            j-=1
            i-=1
        
        i, j = x , y
        #diagonal bottom left
        while j >= 0 and j < 8 and i >= 0 and i < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            j-=1
            i+=1
        
        i, j = x , y
        #diagonal top right
        while j >= 0 and j < 8 and i >= 0 and i < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            j+=1
            i-=1
        
        i, j = x , y
        #diagonal bottom right
        while j >= 0 and j < 8 and i >= 0 and i < 8:
            if board[i][j] == 1:
                attackers.append([i,j])
                break
            j+=1
            i+=1
                          
        return attackers