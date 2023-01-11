class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n - 1: 
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
                n -= 1
            else:
                i += 1
        
        return n