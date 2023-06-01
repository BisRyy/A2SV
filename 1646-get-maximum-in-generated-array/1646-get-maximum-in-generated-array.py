class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        nums = [0,1]
        for i in range(1,n):
            nums.append(nums[i])
            nums.append(nums[i] + nums[i+1])
        return(max(nums[:n+1]))