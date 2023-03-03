class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 0
        right = x//2
        
        while left <= right:
            mid = (left + right) // 2
            
            if mid * mid == x:
                return int(mid)
            elif mid * mid > x:
                right = mid -1
            else:
                left = mid +1
            
        return right