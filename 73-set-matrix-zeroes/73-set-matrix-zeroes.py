class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zeros = []
        
        for i in range(m):
            
            for j in  range(n):
                
                if matrix[i][j] == 0:
                    zeros.append([i,j])
        
        for zero in zeros:
            
            # Horizontal
            for x in range(m): 
                matrix[x][zero[1]] = 0
                
            # Vertical
            for x in range(n):
                matrix[zero[0]][x] = 0
        
        
                
        