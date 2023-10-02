class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0]*(target + 1)
        dp[0] = 1
        for index in range(len(dp)):
            for num in nums:
                if num <= index:
                    dp[index] += dp[index - num]
        return dp[target]