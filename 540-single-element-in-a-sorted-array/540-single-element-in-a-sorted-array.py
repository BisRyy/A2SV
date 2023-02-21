class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        for idx in range(0,len(nums)-1,2):
            if nums[idx] != nums[idx+1]:
                return nums[idx]
            
        return nums[-1]