class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return
            if board[i][j] == 'O':
                board[i][j] = 'T'
                dfs(board, i-1, j)
                dfs(board, i+1, j)
                dfs(board, i, j-1)
                dfs(board, i, j+1)
        
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        for i in range(m):
            dfs(board, i, 0)
            dfs(board, i, n-1)
        for j in range(n):
            dfs(board, 0, j)
            dfs(board, m-1, j)
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
        

        
        