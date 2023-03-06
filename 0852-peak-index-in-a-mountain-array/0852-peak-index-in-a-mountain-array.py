class Solution:
    def peakIndexInMountainArray(self, nums: List[int]) -> int:
        
        left = 1
        right = len(nums) - 2
        
        while left <= right:
            mid = left +  ( right - left) // 2
            if nums[mid - 1] < nums[mid] > nums[mid +  1]:
                return mid
            elif  nums[mid - 1] < nums[mid]:
                left =  mid + 1
            else:
                right = mid 
                
        return 0