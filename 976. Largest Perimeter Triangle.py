class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        for index in range(len(nums)-1,1,-1):
            if nums[index ] < nums[index-1] + nums[index - 2]:
                return nums[index ] + nums[index-1] + nums[index - 2]
            
        return 0
