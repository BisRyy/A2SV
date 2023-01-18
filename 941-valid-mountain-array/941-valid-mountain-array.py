class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        
        maximum = max(arr)
        maxindex = arr.index(maximum)
            
        c = 0
        if maxindex != 0 and maxindex != len(arr)-1 and arr.count(maximum) == 1 :
            for i in range(maxindex):
                if arr[i] < arr[i+1]:
                    c += 1
                else:
                    c = -10
                    break
            
            for i in range(len(arr)-1, maxindex, -1):
                if arr[i] < arr[i-1]:
                    c += 1
                else:
                    c = -10
                    break
                
            
        if c == len(arr)-1 and len(arr) > 2:
            return True
        else:
            return False
                