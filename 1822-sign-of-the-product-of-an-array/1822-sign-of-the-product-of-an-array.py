class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = 1
        for num in nums:
            p*= num
        if p == 0:
            return 0
        return 1 if p > 1 else -1