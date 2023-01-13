class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]):
            return mat
        
        straight = []
        
        for i in range(len(mat)):

            for j in range(len(mat[0])):
                straight.append(mat[i][j])
                
        idx = 0
        reshaped = [[0]*c for  _ in range(r)]
        
        for i in range(r):
            
            for j in range(c):
                reshaped[i][j] = straight[idx]
                idx+=1
                
        del straight
        return reshaped