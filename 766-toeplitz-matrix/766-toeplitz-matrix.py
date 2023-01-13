class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        
        diagonal = defaultdict(set)
        
        for row in range(len(matrix)):
            
            for col in range(len(matrix[0])):
                diagonal[row - col].add(matrix[row][col])
                
                if len(diagonal[row - col]) > 1:
                    return False
                
        return True