class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        
        def cmp(x,y):
            if x > y:
                return -1
            elif x < y:
                return 1
            else:
                return 0
        left = 0
        ans = 1
        
        for index in range(1, len(arr)):
            c = cmp(arr[index - 1], arr[index])
            if c == 0:
                left = index
            
            elif index == len(arr) - 1 or c * cmp(arr[index], arr[index + 1]) != -1:
                ans = max(ans, index - left + 1)
                left = index
            
        return ans