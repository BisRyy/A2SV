class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        r = len(matrix) + 1
        c = len(matrix[0]) +1
        
        self.a = [[0]*(c) for u in range(r)]
        
        for i in range(1,r):
            rsum = 0
            for j in range (1,c):
                rsum += matrix[i-1][j-1]
                self.a[i][j] = rsum + self.a[i-1][j]
                
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        a = self.a
        return a[row2+1][col2+1] - a[row1][col2+1] - a[row2+1][col1] + a[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)