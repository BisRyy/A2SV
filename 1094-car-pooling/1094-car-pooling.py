class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pre = [0]*1001
        
        for trip in trips:
            pre[trip[1]]+=trip[0]
            pre[trip[2]]-=trip[0]
            
        for i in range(1,len(pre)):
            pre[i] += pre[i-1] 
        
        return max(pre) <= capacity
            