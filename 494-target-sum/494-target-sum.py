class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        memo = [0] * (2* total + 1)
        memo[nums[0] + total] += 1       
        memo[-nums[0] + total] += 1
        
        for i in range(1, n):
            new = [0] * (2* total + 1)
            for j in range(-total, total+1):
                if memo[j + total] > 0:
                    new[j + nums[i] + total] += memo[j + total]
                    new[j - nums[i] + total] += memo[j + total]
            memo = new
        return 0 if abs(target) > total else memo[target + total]
                    