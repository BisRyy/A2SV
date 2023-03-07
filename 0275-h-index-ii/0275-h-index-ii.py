class Solution:
    def hIndex(self, n: List[int]) -> int:
        
        left = 0
        right = len(n)-1
        
        while left <= right:
            mid  = left + (right - left) // 2
            
            if n[mid] >= len(n) - mid:
                right = mid - 1
            else:
                left = mid + 1

        return len(n) - left
            