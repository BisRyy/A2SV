class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        n = len(arr)
        temp = 0
        maximum = - 1 
        
        for i in range(n-1, -1, -1):
            temp = arr[i]
            arr[i] = maximum
            maximum = max(maximum, temp)
            
        return arr