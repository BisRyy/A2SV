class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        d = {0:1}
        ans = 0
        total = 0
        
        for num in nums:
            total+=num
            ans += d.get(total-k, 0)
            d[total] = d.get(total, 0) +1
            
        return ans