class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def hours(k):
            hours = 0
            for pile in piles:
                hours += ceil(pile / k)
            return hours
                
        left = 1 
        right = max(piles)
        
        while left <= right:
            k = (left + right)  // 2
        
            if hours(k) <= h:
                right = k - 1
            else:
                left = k + 1
                
        return left