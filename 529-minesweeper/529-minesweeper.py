class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        m, n = len(board), len(board[0])
        x, y = click
        def dfs(x, y):
            mines = 0
            if x < 0 or x >= m or y < 0 or y >= n or board[x][y] != "E":
                return
            for newX, newY in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                if  0 <= x+newX < m and 0 <= y+newY < n and board[x+newX][y+newY] == "M":
                    mines += 1
            if mines == 0:
                board[x][y] = "B"
            else:
                board[x][y] = str(mines)
                return
            for newX, newY in [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]:
                dfs(x+newX, y+newY)
            return
        if board[x][y] == "M":
            board[x][y] = "X"
        else:
            dfs(x, y)
        return board