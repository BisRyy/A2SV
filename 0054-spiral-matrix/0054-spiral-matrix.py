class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)-1
        n = len(matrix[0])-1
        i = 0
        answer = []
        size = (m+1)*(n+1)
        
        if m == 0:
            return matrix[0]

        while i < n//2 + 1:
            for x in range(i,n+1-i):
                if i <= m:
                    answer.append(matrix[i][x])
                else:
                    break

            for y in range(i+1, m-i):
                if i <= n:
                    answer.append(matrix[y][n-i])
                else:
                    break

            for x in range(n-i,-1+i, -1):
                if i <= m:
                    answer.append(matrix[m-i][x])
                else:
                    break

            for y in range(m-1-i, i,-1):
                if i <= n:
                    answer.append(matrix[y][i])
                else:
                    break

            i+=1

        return answer[:size]