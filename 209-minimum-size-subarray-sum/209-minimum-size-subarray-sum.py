class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        left = 0
        total = 0
        answer = float("inf")
        
        for i in range(len(nums)):
            total+=nums[i]
            
            while total >= target:
                answer = min(answer, i - left + 1)
                total-=nums[left]
                left+=1
                
        if answer == float("inf"):
            return 0
        
        return answer 