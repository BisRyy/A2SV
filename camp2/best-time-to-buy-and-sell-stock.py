class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        ans = 0
        
        
        while left <= right < len(prices):
            if prices[right] - prices[left] < 0:
                left = right
            ans = max(ans, prices[right]-prices[left])
            right+=1
        return ans