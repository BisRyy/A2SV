class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        '''
            matrix = [
                        [5,1,9,11],
                        [2,4,8,10],
                        [13,3,6,7],
                        [15,14,12,16]
                    ]
            Output = [
                        [15,13,2,5],
                        [14,3,4,1],
                        [12,6,8,9],
                        [16,7,10,11]
                    ]
        '''
        a = []
        for i in range(len(matrix)):
            m = []
            for j in range(len(matrix[0])):
                m.append(matrix[j][i])
            a.append(m[::-1])
            
        for i in range(len(matrix)):
            m = []
            for j in range(len(matrix[0])):
                matrix[i][j] = a[i][j]
                
        del a