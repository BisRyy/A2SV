class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        def check(d):
            add = 0
            for num in nums:
                add += ceil(num / d)
            return add <= threshold
        
        left = 1
        right = max(nums)
        
        while left < right:
            mid  = left + (right - left) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
            
            