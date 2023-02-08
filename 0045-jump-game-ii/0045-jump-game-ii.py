class Solution:
    def jump(self, nums: List[int]) -> int:
        
        answer, n = 0, len(nums)
        cur, end = 0, 0
        
        for i in range(n - 1):
            
            end = max(end, i + nums[i])

            if i == cur:
                answer += 1
                cur = end
                
        return answer