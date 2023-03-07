class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        def check(t):
            total = 0
            for i in time:
                total += t // i
            return total >= totalTrips
        
        left = 1
        right = max(time) * totalTrips
        
        while left < right:
            mid = left + (right - left) // 2
            
            if check(mid):
                right = mid
            else:
                left = mid + 1
                
        return left