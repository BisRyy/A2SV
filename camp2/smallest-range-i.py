class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        m = max(nums)
        n = min(nums)        
        return (max(m-n - k-k, 0))