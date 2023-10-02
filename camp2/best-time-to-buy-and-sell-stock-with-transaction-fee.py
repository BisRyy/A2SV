class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp, dpPrev = [0, 0], [0, 0]
        for i in range(n-1, -1, -1):
            for j in range(2):
                if j == 1:
                    dp[j] = max(dpPrev[j], dpPrev[0] - prices[i])
                else:
                    dp[j] = max(dpPrev[j], dpPrev[1] + prices[i] - fee)
            dpPrev = dp
        return dpPrev[1]