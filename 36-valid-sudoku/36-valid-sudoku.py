class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        count = defaultdict(int)
        for i in range(9):
            for k in count:
                count[k]=0
                
            for j in range(9):
                if board[i][j] != ".":
                    if 0 < int(board[i][j]) < 10:
                        if count[board[i][j]] == 0:
                            count[board[i][j]] += 1
                        else:
                            return False
                    else:
                        return False

        for j in range(9):
            for k in count:
                count[k]=0
                
            for i in range(9):
                if board[i][j] != ".":
                    if count[board[i][j]] == 0:
                        count[board[i][j]] += 1
                    else:
                        return False

        for i in range(9):
            if i in [0,3,6]:
                for k in count:
                    count[k]=0

            for j in range(3):
                if board[i][j] != ".":
                    if count[board[i][j]] == 0:
                        count[board[i][j]] += 1
                    else:
                        return False

        for i in range(9):
            if i in [0,3,6]:
                for k in count:
                    count[k]=0

            for j in range(3,6): 
                if board[i][j] != ".":
                    if count[board[i][j]] == 0:
                        count[board[i][j]] += 1
                    else:
                        return False

        for i in range(9):
            if i in [0,3,6]:
                for k in count:
                    count[k]=0

            for j in range(6,9):
                if board[i][j] != ".":
                    if count[board[i][j]] == 0:
                        count[board[i][j]] += 1
                    else:
                        return False

        return True