class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left =  0
        right = 0
        answer = -float("inf")
        sum = 0
        while right < k-1:
            sum += nums[right]
            right += 1
        
        while right < len(nums):
            
            sum += nums[right]
            right += 1
            answer = max(answer, sum/k)
            sum -= nums[left]
            left += 1
            
        return answer
            
            
            