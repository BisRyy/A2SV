class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def sums(term, idx):
            if idx == len(nums):
                return term            
            
            x = sums(term, idx + 1)
            y = sums(term ^ nums[idx], idx + 1)
            return x + y
        
        return sums(0, 0)