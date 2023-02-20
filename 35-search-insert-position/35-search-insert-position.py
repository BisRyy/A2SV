class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        for i, j in enumerate(nums):
            if j >= target:
                return i
        return len(nums)