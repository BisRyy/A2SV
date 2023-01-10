class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        answer = []
        diagonals = defaultdict(list)
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diagonals[row+col].append(mat[row][col])
        
        for diagonal in diagonals:
            
            if diagonal % 2 == 0:
                for item in range(len(diagonals[diagonal])-1, -1, -1):
                    answer.append(diagonals[diagonal][item])
                    
            else:
                for item in range(len(diagonals[diagonal])):
                    answer.append(diagonals[diagonal][item])
        
        return answer
