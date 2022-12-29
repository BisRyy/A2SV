class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        result = 0
        
        for index in range(len(nums)):
            temp = (index + 1)^nums[index];
            result ^= temp
            
        return result
