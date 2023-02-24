class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        pre = [0] * (len(nums)+1)
        
        for request in requests:
            pre[request[0]]+=1
            pre[request[1]+1]-=1
            
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
            
        pre = sorted(pre, reverse=True)
        nums = sorted(nums, reverse=True)
        
        ans = 0
        for i in range(len(nums)):
            ans += nums[i]*pre[i]
            
        mod = 10**9 + 7
        return ans % mod 
            
            