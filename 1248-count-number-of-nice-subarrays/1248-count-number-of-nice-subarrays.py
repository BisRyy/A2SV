class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odds = [nums[0]%2]*len(nums)
        
        for i in range(1,len(nums)):
            odds[i] = odds[i-1] + nums[i] % 2
            
        c = Counter([0]+odds)
        d = 0
        for i in c:
            if i >= k:
                d +=c[i] * c.get(i-k, 0)
        return d