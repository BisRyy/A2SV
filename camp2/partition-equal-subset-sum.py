class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        s = sum(nums)
        
        if s%2 == 1:
            return False
        
        dp = set([0])
        for num in nums:
            newdp = set()
            for t in dp:
                newdp.add(t)
                newdp.add(t+num)
            dp = newdp
        
        return s//2 in dp
            