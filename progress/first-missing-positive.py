class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.sort()
        ans=1
        for i in range(len(nums)):
            if nums[i] == ans:
                ans += 1
        return ans