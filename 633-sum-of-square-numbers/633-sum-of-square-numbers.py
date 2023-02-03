class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        i = 0
        j = sqrt(c)//1
        
        while i <= j:
            if j*j + i*i == c:
                return True
            elif j*j + i*i > c:
                j-=1
            else:
                i+=1
                
        return False
            