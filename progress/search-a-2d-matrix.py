class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        m, n = len(matrix), len(matrix[0])
        
        for row in range(0,m):
            if matrix[row][0] == target:
                return True
            elif matrix[row][0] > target:
                for col in range(n):
                    if matrix[row - 1][col] == target:
                        return True
            else:
                for col in range(n):
                    if matrix[row][col] == target:
                        return True
        return False
                
                    
        