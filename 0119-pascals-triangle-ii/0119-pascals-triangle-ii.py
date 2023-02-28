class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        def pascal(y, n):
            if len(y) == n+1:
                return y
            
            list = []
            for i in range(len(y)-1):
                list.append(y[i]+y[i+1])
                
            return pascal([1]+list+[1],n)
        
        if rowIndex == 0:
            return [1]
        
        if rowIndex == 1:
            return [1,1]
        
        y = [1,1]
        
        return(pascal(y,rowIndex))
        