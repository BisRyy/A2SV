class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zero = 0
        for num in nums:
            if num == 0:
                zero += 1
            else:
                prod *= num
            
        for i in range(len(nums)):
            if nums[i] != 0 and zero > 0:
                nums[i] = 0
            elif nums[i] == 0 and zero == 1:
                nums[i] = prod
            elif zero > 1:
                nums[i] = 0
            else:
                nums[i] = prod // nums[i]
            
        return nums