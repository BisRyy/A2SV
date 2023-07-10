class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) - 1
        
        maximum = 0
        while left <= right :
            x = min(height[left], height[right])
            y = right - left
            
            maximum = max(x*y, maximum)
            
            if height[left] > height[right]:
                right-=1
            else:
                left+=1
                
        return maximum
            