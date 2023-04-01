class Solution:
    def search(self,nums:List[int],target:int)->int:
        x = bisect_left(nums, target)
        return x if x < len(nums) and nums[x] == target else -1